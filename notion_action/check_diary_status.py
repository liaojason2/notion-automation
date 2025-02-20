import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def get_today_date() -> str:
    """Return today's date in YYYY-MM-DD format."""
    return datetime.datetime.now().strftime("%Y-%m-%d")

def fetch_notion_entries() -> list:
    """
    Query Notion database and return results list.
    Raises an exception if request fails.
    """
    query_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(query_url, headers=HEADERS)
    #response.raise_for_status()
    return response.json().get("results", [])

def diary_check() -> str:
    """
    Check if today and yesterday's diary entry exists in Notion.
    Sends Telegram notification about result.
    """
    results = fetch_notion_entries()
    if not results:
        return "No results found in Notion."

    # Placeholder pattern for today's title
    title_pattern = "${date} 日記"

    # Extract current entry title
    today_diary_title = results[0]["properties"]["標題"]["title"][0]["text"]["content"]
    today_diary_link = results[0]["url"]
    yesterday_diary_title = results[1]["properties"]["標題"]["title"][0]["text"]["content"]
    yesterday_diary_link = results[1]["url"]

    message = ""

    if today_diary_title == title_pattern:
        message += "今天的日記還沒有完成喔 ⬇️\n" + today_diary_link

    message += "\n\n"

    if yesterday_diary_title == title_pattern:
        message += "昨天的日記還沒有完成！\n" + yesterday_diary_link

    return message
   