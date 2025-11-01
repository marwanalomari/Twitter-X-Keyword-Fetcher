# 🐍 Twitter (X) Keyword Fetcher
A simple **Python script** that fetches recent posts from **X (formerly Twitter)** based on specific keywords using the official **X API v2**.  
The script saves tweets — including author name, username, date, and text — into a local `tweets.txt` file.

This project is built **for learning purposes**, to explore how APIs work and how to handle rate limits gracefully.

---

## ✨ Features
- Fetches recent tweets containing specific keywords or hashtags  
- Saves tweets locally to a `.txt` file  
- Includes author **name** and **username**  
- Automatically waits and retries if the **rate limit** is reached  
- Simple and lightweight — no database required  

---

## 🧰 Requirements
- **Python 3.8+**
- **Tweepy** library  
  Install it using:
  ```bash
  pip install tweepy

⚙️ Setup
1. Clone this repository
git clone https://github.com/marwanalomari/Twitter-X-Keyword-Fetcher.git
cd x-keyword-fetcher

2. Create a Developer Account on X
Visit https://developer.x.com
 and:
- Create a Project and App
- Generate a Bearer Token
- Copy it for use in your script

3. Edit the script
Open fetch_tweets.py and replace:
BEARER_TOKEN = "YOUR_BEARER_TOKEN"

4. Customize your search keywords
SEARCH_KEYWORDS = "gaming OR esports"
You can replace this with any keywords or hashtags you like.

▶️ Run the Script
python fetch_tweets.py

The script will:
- Fetch up to 20 recent tweets (default: MAX_RESULTS = 20)
- Wait and retry automatically if rate-limited
- Save results to tweets.txt

Example output:
Name: Alex Johnson
Username: @alex_gamer
Date: 2025-11-01 14:21:35+00:00
Tweet: Just watched an epic esports match today! 🔥
------------------------------------------------------------

⚠️ Rate Limits
If you’re using the free X API, requests are limited (around 50 per 15 minutes).
The script will automatically:
- Detect when you hit the limit
- Wait 15 minutes
- Retry once

To avoid frequent rate limits, you can:
- Lower MAX_RESULTS
- Wait longer between runs
- Upgrade to Basic access on developer.x.com

💡 Future Improvements
- Add CSV export for data analysis
- Store results in a SQLite or MongoDB database
- Include more user info (e.g., profile image, verified status)
- Build a web dashboard to visualize fetched tweets

🧠 License
This project is licensed under the MIT License — feel free to use and modify it for your own learning or projects.

👤 Author
Marwan Al Omari
Created for educational purposes to explore X API and Python data fetching.
---
