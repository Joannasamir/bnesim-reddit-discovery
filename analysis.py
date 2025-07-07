from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from llm_config import llm


load_dotenv()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt = PromptTemplate.from_template("""
You are an assistant that classifies Reddit posts.

Post:
{post_text}

Classify the post into:
- Question
- Complaint
- Recommendation request
- General discussion
- Praise
- Spam

Also classify the sentiment: Positive, Negative, or Neutral.

Return in JSON format like:
{{ "intent": "...", "sentiment": "..." }}
""")

chain = prompt | llm

# def analyze_post(post_text):
#     result = chain.invoke({"post_text": post_text})
#     return result

def analyze_post(post_text):
    raw_response = chain.invoke({"post_text": post_text})
    return extract_json_from_response(raw_response.content if hasattr(raw_response, "content") else str(raw_response))


from discovery import fetch_posts  # Import your fetch_posts function
from analysis import analyze_post  # Import your analyze_post function

if __name__ == "__main__":
    posts = fetch_posts()
    print(f"Found {len(posts)} relevant posts.\n")
    for i, p in enumerate(posts[:5]):  # Just the first 5 for testing
        print(f"[{i+1}] Title: {p['title']}")
        print(f"Content: {p['content']}\n")
        classification = analyze_post(p['title'] + "\n" + p['content'])
        print(f"Classification: {classification}\n")
        print("-" * 60)

import json
import re

def extract_json_from_response(response_text):
    try:
        match = re.search(r'\{.*?\}', response_text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"[Parsing error] {e}")
    return {"intent": "Unknown", "sentiment": "Unknown"}
