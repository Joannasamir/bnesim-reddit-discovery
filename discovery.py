import praw
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from llm_config import llm


load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Travel eSIM, international roaming, travel connectivity
# Specific mentions of "BNESIM" or competitors
# Posts asking for travel SIM recommendations
# Complaints about roaming charges or connectivity issues

KEYWORDS = [
    "eSIM", "travel sim", "BNESIM", "Airalo", "Ubigi",
    "international roaming", "connectivity issue", "roaming charges", "travel connectivity", "roaming", "bn",
    "data plan", "connectivity"
]

#KEYWORDS = ["esim", "sim", "roaming", "bn", "bnesim", "travel sim", "data plan", "connectivity"]


def fetch_posts(subreddits=["travel", "digitalnomad","techsupport","eSIM","japantravel","solotravel",
    'backpacking','onebag','TravelHacks', 'overlanding','NoContract','Android',
    'ItalyTravel','EuropeTravel'], days=1000):
    results = []
    time_threshold = datetime.utcnow() - timedelta(days=days)

    for subreddit in subreddits:
        for post in reddit.subreddit(subreddit).new(limit=300):
            if datetime.utcfromtimestamp(post.created_utc) < time_threshold:
                continue
            if any(keyword.lower() in post.title.lower() + post.selftext.lower() for keyword in KEYWORDS):
                results.append({
                    "title": post.title,
                    "content": post.selftext,
                    "url": post.url,
                    "subreddit": post.subreddit.display_name,
                    "upvotes": post.score,
                    "comments": post.num_comments,
                    "created_utc": post.created_utc
                })
    return results

if __name__ == "__main__":
    posts = fetch_posts()
    print(f"Found {len(posts)} relevant posts.\n")
    for p in posts:
        print(f"Title: {p['title']}")
        print(f"Subreddit: {p['subreddit']}")
        print(f"URL: {p['url']}")
        print(f"Upvotes: {p['upvotes']} | Comments: {p['comments']}")
        print("-" * 60)

# import requests
# from datetime import datetime, timedelta, timezone
# from dotenv import load_dotenv
# import os

# load_dotenv()

# import praw

# reddit = praw.Reddit(
#     client_id=os.getenv("REDDIT_CLIENT_ID"),
#     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
#     user_agent=os.getenv("REDDIT_USER_AGENT")
# )

# subreddit = reddit.subreddit('travel')
# for submission in subreddit.search("eSIM", time_filter='month', sort='new', limit=30):
#     print(submission.title, submission.url)


# KEYWORDS = [
#     "eSIM", "travel sim", "BNESIM", "Airalo", "Ubigi",
#     "international roaming", "connectivity issue", "roaming charges",
#     "travel connectivity", "roaming", "bn", "data plan", "connectivity"
# ]

# SUBREDDITS = [
#     "travel", "solotravel", "digitalnomad", "techsupport", "eSIM", "JapanTravel",
#     "backpacking", "onebag", "TravelHacks", "overlanding", "NoContract", "Android",
#     "AppleWatch", "Thailand", "Vietnam", "Europe", "ItalyTravel", "EuropeTravel"
# ]

# def fetch_posts(keywords=KEYWORDS, subreddits=SUBREDDITS, days=30, limit_per_query=50):
#     results = []
#     end_time = int(datetime.utcnow().timestamp())
#     start_time = int((datetime.utcnow() - timedelta(days=days)).timestamp())

#     for keyword in keywords:  
#         for subreddit in subreddits:
#             url = (
#                 f"https://api.pushshift.io/reddit/search/submission/?q={keyword}"
#                 f"&subreddit={subreddit}&after={start_time}&before={end_time}"
#                 f"&size={limit_per_query}&sort=desc"
#             )


#             try:
#                 res = requests.get(url, timeout=10)
#                 res.raise_for_status()
#                 data = res.json().get("data", [])
#                 for post in data:
#                     if not post.get("title"):
#                         continue  # skip empty titles
#                     results.append({
#                         "title": post.get("title", ""),
#                         "content": post.get("selftext", ""),
#                         "url": f"https://www.reddit.com{post.get('permalink', '')}",
#                         "subreddit": post.get("subreddit", ""),
#                         "upvotes": post.get("score", 0),
#                         "comments": post.get("num_comments", 0),
#                         "created_utc": post.get("created_utc", 0)
#                     })

#             except Exception as e:
#                 print(f"Failed to fetch from subreddit '{subreddit}' with keyword '{keyword}': {e}")
#                 continue

#     return results

# # Test runner
# if __name__ == "__main__":
#     posts = fetch_posts(days=30, limit_per_query=30)
#     print(f"✅ Found {len(posts)} posts.\n")

#     for i, p in enumerate(posts[:10]):
#         print(f"[{i+1}] {p['title']}")
#         print(f"Subreddit: {p['subreddit']}")
#         print(f"Upvotes: {p['upvotes']} | Comments: {p['comments']}")
#         print(f"URL: {p['url']}")
#         print("-" * 80)
