import telebot
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize bot
bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

# Handler for all messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.chat.id
    print(f"Chat ID: {chat_id}")  # Print to console
    bot.reply_to(message, f"Hello World! Your chat ID is: {chat_id}")

if __name__ == "__main__":
    print("Bot started...")
    bot.infinity_polling()