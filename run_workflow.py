from discovery import fetch_posts
from analysis import analyze_post
from response import generate_reply
import json
import csv
from datetime import datetime

import logging

logging.basicConfig(
    filename="run_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def score_post(post, intent):
    base = post["upvotes"] + 2 * post["comments"]
    if intent.lower() == "recommendation request":
        base += 10  # bonus weight
    return base

# Setup file timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# JSON Export Function
def save_to_json(data, filename=f"results_{timestamp}.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# CSV Export Function
def save_to_csv(data, filename=f"results_{timestamp}.csv"):
    keys = data[0].keys()
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Run Workflow
if __name__ == "__main__":
    posts = fetch_posts()
    enriched_posts = []

enriched_posts = []

for i, p in enumerate(posts[:5]):  # Replace 5 with full length if needed
    logging.info(f"Processing post #{i+1}: {p['title'][:50]}...")

    # 1. Try to classify the post
    try:
        classification = analyze_post(p["title"] + "\n" + p["content"])
    except Exception as e:
        logging.error(f"Failed to classify post: {e}")
        continue

    # 2. Try to generate a reply
    try:
        reply = generate_reply(p["title"] + "\n" + p["content"])
    except Exception as e:
        logging.error(f"Failed to generate reply: {e}")
        reply = "Sorry, no reply could be generated."

    # 3. Try to score the post
    try:
        score = score_post(p, classification["intent"])
    except Exception as e:
        logging.warning(f"Post skipped due to scoring/parsing issue: {e}")
        continue

    # 4. Add everything to the post dict
    p["intent"] = classification["intent"]
    p["sentiment"] = classification["sentiment"]
    p["score"] = score
    p["reply"] = reply

    enriched_posts.append(p)


enriched_posts = sorted(enriched_posts, key=lambda x: x["score"], reverse=True)

# ✅ Place these 2 lines here AFTER the loop
save_to_json(enriched_posts)
save_to_csv(enriched_posts)
