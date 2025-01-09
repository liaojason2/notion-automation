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

# Function to check if diary entry exists for today and is filled
def check_diary_entry():
    today_date = get_today_date()

    # Query the Notion database to check for today's entry
    query_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(query_url, headers=headers)

    if response.status_code == 200:
        results = response.json()["results"]
        
        # Check if an entry with today's date exists
        for page in results:
            # Assuming the date property is named "Date" or similar
            if "properties" in page and "Date" in page["properties"]:
                date_property = page["properties"]["Date"]
                if date_property["date"]:
                    entry_date = date_property["date"]["start"]
                    if entry_date.startswith(today_date):
                        # Check if the diary content is filled
                        if "properties" in page and "Content" in page["properties"]:
                            content_property = page["properties"]["Content"]
                            if content_property.get("rich_text"):
                                content = content_property["rich_text"]
                                if content:  # If content is not empty
                                    print("Your diary is filled for today.")
                                    return
        print("No diary entry found for today or it's empty.")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Run the check
check_diary_entry()
