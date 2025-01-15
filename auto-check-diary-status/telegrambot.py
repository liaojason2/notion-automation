import asyncio
import os
from dotenv import load_dotenv
import telegram
from telegram.error import TelegramError

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

async def send_message(msg: str, chat_id: str, token: str) -> None:
    """
    Sends a message to a Telegram user or group.

    Args:
        msg (str): Text of the message to be sent. Max 4096 characters.
        chat_id (str): Unique identifier or username (e.g., '@channelusername').
        token (str): Bot's unique authentication token.
    """
    try:
        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=msg)
        print("Message Sent!")
    except TelegramError as e:
        print(f"Failed to send message: {e}")

if __name__ == "__main__":
    message_string = "Testing from virtual server"
    print(message_string)
    asyncio.run(send_message(msg=message_string, chat_id=TELEGRAM_CHAT_ID, token=TELEGRAM_BOT_TOKEN))