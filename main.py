from src import check_diary_status, telegram_bots
import functions_framework

@functions_framework.http
def main(request):
  check_diary_status.diary_check()
  return "Diary check completed."