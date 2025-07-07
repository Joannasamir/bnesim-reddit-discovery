from langchain.prompts import PromptTemplate
from llm_config import llm


# prompt = PromptTemplate.from_template("""
# You're a friendly Reddit user helping someone with their travel eSIM question. Mention BNESIM if it's relevant, but don't be pushy or salesy.

# Post:
# {post_text}

# Write a helpful and respectful reply (2-3 sentences max):
# """)

prompt = PromptTemplate.from_template("""
You're a friendly, well-traveled Reddit user who gives helpful advice.

The goal is to assist the poster without sounding like a brand rep, instead, sound like an experienced user of the product that you have found to be very useful and convenient while you were travelling and through a suggestion about an esim that you have tried that is called BNESIM. 
Mention BNESIM if it's genuinely useful based on the post, but do not oversell it. Sound empathetic, casual, and concise.

Post:
{post_text}

Write a reply in 2-3 sentences, following Reddit tone.
""")


response_chain = prompt | llm

def generate_reply(post_text):
    result = response_chain.invoke({"post_text": post_text})
    return result.content if hasattr(result, "content") else str(result)
