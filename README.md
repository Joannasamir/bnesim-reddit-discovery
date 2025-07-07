# BNESIM Reddit Opportunity Discovery Tool

This project identifies marketing opportunities on Reddit for BNESIM, a global eSIM provider. It searches for recent Reddit posts related to travel eSIMs, connectivity issues, roaming complaints, or competitors (like Airalo and Ubigi). Each relevant post is analyzed using AI to determine its intent and sentiment, then a natural, respectful response is generated—ready for review or direct engagement by the marketing team.

---

Features

- ✅ **Reddit Discovery Engine**  
  Finds recent posts from key travel-related subreddits using relevant keywords (e.g., “eSIM”, “BNESIM”, “roaming charges”).

- ✅ **AI-Powered Content Analysis**  
  Classifies each post’s intent (e.g., question, complaint, recommendation request) and sentiment (positive, negative, neutral).

- ✅ **AI Response Generation**  
  Generates concise, empathetic, and helpful replies using GPT, tailored for Reddit tone and etiquette.

- ✅ **Opportunity Scoring**  
  Prioritizes posts using a relevance score based on engagement (upvotes/comments), intent, and sentiment.

- ✅ **Logging & Error Handling**  
  Logs processing status, failures, and debug information to `run_log.txt`.

- ✅ **Data Export**  
  Saves results to both `.json` and `.csv` files for team review.

---

## 📦 Output Files

- `results_<timestamp>.json` — full post metadata + AI analysis
- `results_<timestamp>.csv` — human-readable format for marketing team
- `run_log.txt` — log of each run (successes, skips, errors)

---

## 🧰 Tech Stack

- Python
- [PRAW](https://praw.readthedocs.io/) – Reddit API Wrapper
- [LangChain](https://www.langchain.com/) – Prompt chaining and LLM integration
- [OpenAI](https://platform.openai.com/) – GPT-3.5-turbo for classification & replies
- dotenv – Secure API key loading
- Streamlit (optional) – For basic UI (optional)

