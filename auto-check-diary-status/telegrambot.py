import asyncio
import os
from dotenv import load_dotenv
import telegram
from telegram.error import TelegramError

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

async def send(msg, chat_id, token):
    """
    Send a message "msg" to a telegram user or group specified by "chat_id"
    msg         [str]: Text of the message to be sent. Max 4096 characters after entities parsing.
    chat_id [int/str]: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    token       [str]: Bot's unique authentication token.
    """
    bot = telegram.Bot(token=token)
    await bot.sendMessage(chat_id=chat_id, text=msg)
    print('Message Sent!')

MessageString = 'Testing from virtual server'
print(MessageString)
asyncio.run(send(msg="MessageString", chat_id=TELEGRAM_CHAT_ID, token=TELEGRAM_BOT_TOKEN))