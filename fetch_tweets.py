import tweepy
import time

# === CONFIGURATION ===
BEARER_TOKEN = "YOUR_BEARER_TOKEN"   # Replace with your token from developer.x.com
SEARCH_KEYWORDS = "gaming OR esports" # Change keywords as you like
MAX_RESULTS = 5                      # Number of tweets to fetch (max 100 per call)
OUTPUT_FILE = "tweets.txt"

# === SETUP CLIENT ===
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets():
    """Fetch recent tweets and return the response."""
    return client.search_recent_tweets(
        query=SEARCH_KEYWORDS,
        max_results=MAX_RESULTS,
        tweet_fields=["created_at", "lang", "author_id"],
        user_fields=["username", "name"],
        expansions=["author_id"]
    )

# === FETCH WITH RETRY HANDLING ===
print(f"Fetching tweets containing: {SEARCH_KEYWORDS}")
try:
    response = fetch_tweets()
except tweepy.errors.TooManyRequests:
    print("⚠️ Rate limit reached. Waiting 15 minutes before retrying...")
    time.sleep(15 * 60)
    print("Retrying now...")
    response = fetch_tweets()

# === MAP USERS ===
users = {user.id: user for user in response.includes["users"]} if response.includes else {}

# === SAVE RESULTS ===
if not response.data:
    print("No tweets found for the given keywords.")
else:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for tweet in response.data:
            user = users.get(tweet.author_id)
            username = user.username if user else "Unknown"
            name = user.name if user else "Unknown"

            f.write(f"Name: {name}\n")
            f.write(f"Username: @{username}\n")
            f.write(f"Date: {tweet.created_at}\n")
            f.write(f"Tweet: {tweet.text}\n")
            f.write("-" * 60 + "\n")

    print(f"✅ Saved {len(response.data)} tweets (with usernames) to {OUTPUT_FILE}")