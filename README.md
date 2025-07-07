
# 🔎 BNESIM Reddit Opportunity Discovery Tool

This AI-powered tool discovers recent Reddit posts about travel eSIMs, international roaming, connectivity issues, and BNESIM competitors. It classifies post intent and sentiment, scores engagement potential, and generates friendly, on-brand reply suggestions for BNESIM’s marketing team.


## AT THE END, YOU WILL FIND A DRIVE LINK WITH A VIDEO OF THE DEMO, JUST IN CASE YOU DO NOT WANT TO GO THROUGH THE HASSLE OF SETTING UP :) 
---

## 🚀 Features

- 🔍 Pulls Reddit posts via Pushshift API
- 🎯 Keyword filtering for travel eSIMs, roaming, connectivity
- 🧠 LangChain + OpenAI GPT-based post classification (intent + sentiment)
- 💬 Generates natural, Reddit-style replies that mention BNESIM when relevant
- 📈 Relevance scoring with sentiment boost
- 📄 Exports results to CSV and JSON
- 🌐 Optional Streamlit web interface

---

## 📂 Project Structure

```

bnesim-reddit-discovery/
├── discovery.py         # Reddit post fetching
├── analysis.py          # Post classification (intent + sentiment)
├── response.py          # Reply generation using LangChain
├── llm\_config.py        # OpenAI LLM setup
├── run\_workflow\.py      # Main pipeline (discovery → analysis → response → export)
├── app.py               # Streamlit web app
├── requirements.txt     # Dependencies
├── .env.example         # Sample environment variables
└── README.md            # This file

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Joannasamir/bnesim-reddit-discovery.git
cd bnesim-reddit-discovery
````

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API keys

Create a `.env` file in the project root based on this template:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=BNESIMDiscoveryBot
OPENAI_API_KEY=your_openai_api_key
```

---

## 🧪 How to Use

### Run the full pipeline from terminal:

```bash
python run_workflow.py
```

This will:

* Fetch relevant Reddit posts
* Analyze each post (intent + sentiment)
* Generate a helpful AI reply
* Score each opportunity
* Save results to `results_TIMESTAMP.csv` and `.json`

---

## 🌐 Launch the Web App

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501) to:

* View total posts retrieved
* See post titles, content, subreddit, upvotes/comments
* Read AI-generated classification and replies
* Download results

---

## 🧠 Scoring Logic

Each post receives a relevance score based on:

* Keyword presence
* Post length and engagement
* Sentiment boost:

  * `Positive` → +3 points
  * `Negative` → −5 points

This helps prioritize which posts are most promising for engagement.

---

## 📁 Exported Outputs

Files are saved automatically:

* `results_YYYYMMDD_HHMMSS.json`
* `results_YYYYMMDD_HHMMSS.csv`

Each record includes:

* Title, content, subreddit
* URL, upvotes, comments
* Intent, sentiment
* AI reply
* Relevance score

---

## ✅ Tech Stack

* Python 3
* LangChain + OpenAI GPT-3.5
* PRAW (Reddit API)
* Pushshift API
* Streamlit (web UI)
* dotenv, TextBlob, CSV/JSON

---

## 🔐 Environment Variables

> ⚠️ Do not commit your `.env` file to GitHub. Use `.env.example` instead.

---

## 👤 Author

**Joanna Samir**
Junior AI Automation Engineer Candidate
[GitHub](https://github.com/Joannasamir) · [LinkedIn](https://www.linkedin.com/in/joannasamir)




