import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

# Notion API headers
headers = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",  # Use the latest version
}

# Function to get today's date in "YYYY-MM-DD" format
def get_today_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

    today_date = get_today_date()
    query_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(query_url, headers=headers)

    if response.status_code == 200:
        results = response.json()["results"]
        title = "${date} 日記"
    else:
