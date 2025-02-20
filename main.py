from notion_action import check_diary_status
from telegram_bot_action import telegram_bot
import asyncio
import functions_framework

@functions_framework.http
def main(request):
  telegram_message = ""
  telegram_message += check_diary_status.diary_check()

  if telegram_message:
    asyncio.run(telegram_bot.send_message(telegram_message))
    return "Success"
  return "Success"