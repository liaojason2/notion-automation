import requests
import datetime
import os
import asyncio
from dotenv import load_dotenv
import src.telegram_bot as telegram_bot

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
    Check if today's diary entry exists in Notion.
    Sends Telegram notification about result.
    """
    results = fetch_notion_entries()
    if not results:
        asyncio.run(telegram_bot.send_message(msg="No results found in Notion."))
        return "No Notion entries."

    # Placeholder pattern for today's title
    title_pattern = "${date} 日記"

    # Extract current entry title
    current_title = results[0]["properties"]["標題"]["title"][0]["text"]["content"]

    if current_title == title_pattern:
        msg = "你還沒有填今天的日記！"
        asyncio.run(telegram_bot.send_message(msg=msg))
        return msg
