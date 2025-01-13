import requests
import datetime
import os
from dotenv import load_dotenv
import functions_framework


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

@functions_framework.http
def diary_check(request):
    NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
    DATABASE_ID = os.getenv("DATABASE_ID")

    headers = {
        "Authorization": f"Bearer {NOTION_API_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    def get_today_date():
        return datetime.datetime.now().strftime("%Y-%m-%d")

    today_date = get_today_date()
    query_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(query_url, headers=headers)

    if response.status_code == 200:
        results = response.json()["results"]
        title = "${date} 日記"
        if (results[0]["properties"]["標題"]["title"][0]["text"]["content"]) != title:
            return "Your diary is filled for today."
        return "No diary entry found for today or it's empty."
    else:
        return f"Error: {response.status_code}, {response.text}"
