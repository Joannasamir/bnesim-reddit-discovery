# 🔎 BNESIM Reddit Opportunity Discovery Tool

This AI-powered tool automatically discovers relevant Reddit posts about travel eSIMs, roaming, and BNESIM's competitors. It classifies each post’s intent and sentiment, then generates community-friendly replies — helping BNESIM’s marketing team identify real opportunities for engagement.

---

## 📌 Project Overview

Reddit is a goldmine for organic travel-related questions and complaints. This tool monitors subreddits for posts about:
- Travel eSIM and connectivity issues
- Competitor mentions (Airalo, Ubigi, etc.)
- International roaming and SIM recommendations
- BNESIM brand mentions

Each post is analyzed and scored to prioritize high-value engagement opportunities.

---

## 🧠 Features

- 🔍 Reddit post discovery via Pushshift API
- 🧵 Extracts post title, content, URL, subreddit, and engagement metrics
- 🧠 Classifies each post (e.g., complaint, praise, question) using LangChain + OpenAI
- 🎭 Performs sentiment analysis (positive/neutral/negative)
- 💬 Generates smart, helpful replies (Reddit tone, soft brand mention)
- 📈 Scores post relevance/opportunity
- 📄 Exports results to CSV and JSON
- 🌐 Optional Streamlit web app for reviewing results

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Joannasamir/bnesim-reddit-discovery.git
cd bnesim-reddit-discovery
