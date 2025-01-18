# Project Overview

This Python project checks daily diary entries on Notion and sends result on Telegram bot.

## Project Structure

It uses [`main.py`](main.py) to define function entrypoint, which calls the `diary_check()` function in [`src/check_diary_status.py`](src/check_diary_status.py). If the diary isn't filled, it sends a reminder via `send_message()` in [`src/telegram_bot.py`](src/telegram_bot.py).

- **main.py**: Functions Framework entry point  
- **src/check_diary_status.py**: Fetches and checks today's diary entry in Notion  
- **src/telegram_bot.py**: Sends Telegram notifications  
- **telegram_group_id.py**: Prints the Telegram chat ID  
- **env.yaml / .env**: Environment variables for the application  
- **requirements.txt**: Python dependencies

## Environment Variables

Add the following variables in your `.env` or `env.yaml`:

- `NOTION_API_TOKEN`  
- `DATABASE_ID`  
- `TELEGRAM_BOT_TOKEN`  
- `TELEGRAM_CHAT_ID`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Populate env.yaml or .env with valid credentials.

Run locally using the Functions Framework:

```shell
functions-framework --target=main
```

Deploy on Google Cloud:

Create a topic:

```shell
gcloud pubsub topics create notion-notify
```

Deploy function:

```shell
gcloud functions deploy notion-automation \
--gen2 \
--runtime=python312 \
--region=asia-east1 \
--source="." \
--entry-point=main \
--trigger-topic=notion-notify \
--env-vars-file="env.yaml"
```

Create scheduler:

```shell
gcloud scheduler jobs create pubsub notion-notify \
--topic=notion-notify \
--schedule="<fill your cron expression>" \
--message-body="." \
--location="asia-east1"
```
