# Notion Automation

Checks daily diary entries on Notion and sends result on Telegram bot. Develop by Python and deploy on Google Cloud Function.

<!-- TOC -->

- [Notion Automation](#notion-automation)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
    - [Install required package](#install-required-package)
    - [Environment Variables](#environment-variables)
    - [Run function locally](#run-function-locally)
    - [Deploy on Google Cloud:](#deploy-on-google-cloud)
  
## Project Structure

It uses [`main.py`](main.py) to define function entrypoint, which calls the `diary_check()` function in [`src/check_diary_status.py`](src/check_diary_status.py). If the diary isn't filled, it sends a reminder via `send_message()` in [`src/telegram_bot.py`](src/telegram_bot.py).

- **main.py**: Functions Framework entry point  
- **src/check_diary_status.py**: Fetches and checks today's diary entry in Notion  
- **src/telegram_bot.py**: Sends Telegram notifications  
- **telegram_group_id.py**: Prints the Telegram chat ID  
- **env.yaml**: Environment variables for the application  
- **requirements.txt**: Python dependencies

## Installation

### Install required package

```bash
pip install -r requirements.txt
```

### Environment Variables

Add the following variables in your `env.yaml`:

- `NOTION_API_TOKEN`  
- `DATABASE_ID`  
- `TELEGRAM_BOT_TOKEN`  
- `TELEGRAM_CHAT_ID`

### Run function locally

```shell
functions-framework --target=main
```

### Deploy on Google Cloud:

```shell
## Create a topic:

gcloud pubsub topics create notion-notify

# Deploy function:

gcloud functions deploy notion-automation \
--gen2 \
--runtime=python312 \
--region=asia-east1 \
--source="." \
--entry-point=main \
--trigger-topic=notion-notify \
--env-vars-file="env.yaml"

# Create scheduler:

gcloud scheduler jobs create pubsub notion-notify \
--topic=notion-notify \
--schedule="* 22 * * *" \ # Run everyday in 10 pm 
--message-body="." \
--location="asia-east1"
```
