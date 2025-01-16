import asyncio
import os
from dotenv import load_dotenv
import telegram
from telegram.error import TelegramError

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

async def send_message(msg: str) -> None:
    """
    Send a message to a Telegram chat
    """
    try:
        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)
        print("Message Sent!")
    except TelegramError as e:
        print(f"Failed to send message: {e}")