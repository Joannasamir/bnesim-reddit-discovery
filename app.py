# import streamlit as st
# from discovery import fetch_posts
# from analysis import analyze_post
# from response import generate_reply

# st.title("BNESIM Reddit Opportunity Discovery")

# if st.button("Fetch & Analyze Posts"):
#     posts = fetch_posts()
#     enriched = []

#     for p in posts[:5]:
#         st.subheader(p["title"])
#         st.write(p["content"])
#         try:
#             result = analyze_post(p["title"] + "\n" + p["content"])
#             reply = generate_reply(p["title"] + "\n" + p["content"])
#             st.success(f"Intent: {result['intent']} | Sentiment: {result['sentiment']}")
#             st.info(f"Suggested Reply:\n{reply}")
#         except Exception as e:
#             st.error(f"Error: {e}")

import streamlit as st
from discovery import fetch_posts
from analysis import analyze_post
from response import generate_reply

st.set_page_config(page_title="BNESIM Reddit Discovery", layout="wide")

st.title("📡 BNESIM Reddit Opportunity Discovery Tool")

# Fetch posts when button clicked
if st.button("🔍 Fetch and Analyze Reddit Posts"):
    posts = fetch_posts()
    st.success(f"✅ {len(posts)} relevant posts found.")

    for i, post in enumerate(posts):
        st.markdown("---")
        st.subheader(f"{i+1}. {post['title']}")

        st.markdown(f"**Subreddit:** r/{post['subreddit']}")
        st.markdown(f"**Upvotes:** {post['upvotes']} | **Comments:** {post['comments']}")
        st.markdown(f"**URL:** [Open Post]({post['url']})")

        st.markdown("**Post Content:**")
        st.write(post["content"] or "_No content_")

        try:
            result = analyze_post(post["title"] + "\n" + post["content"])
            intent = result.get("intent", "Unknown")
            sentiment = result.get("sentiment", "Unknown")

            st.info(f"**Intent:** {intent} | **Sentiment:** {sentiment}")

            reply = generate_reply(post["title"] + "\n" + post["content"])
            st.success("💬 Suggested Reply:")
            st.write(reply)

        except Exception as e:
            st.error(f"Error analyzing post: {e}")

