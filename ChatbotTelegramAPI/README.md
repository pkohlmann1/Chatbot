# Chatbot-Telegram-API

This is the Chatbot-Telegram-API. This needs to run for being able to chat with the Telegram-Bot.
The Bots Telegram name is CustomerSupportChatbot (@customer_support_chatbot)

The Bots API-Token is 5465490826:AAHGe7Q76oXE0STS7QGoWUra5t1CQbuybgw

## Installation (lokales aufsetzen)

Install required packages
```bash
pip install -r requirements.txt
```

Make sure you have all necessary model files for the self-trained model in the model directory. Otherwise use a pre-trained model.
The folder structure should look like this. Model can be downloaded here: https://www.dropbox.com/sh/4jjl7yvipibfsj3/AAAK1j0sQPZNMEGlnjmw5MW8a?dl=0
```
.
+-- Finetuning
|   +-- output_final (Contains all the trained model data)
|   --- main.py
|   --- README.md
|   --- requirements.txt
```

Download Ngrok from https://ngrok.com/
Add this Authtoken to your ngrok config with this line in the terminal
```bash
ngrok config add-authtoken 2DTpPwg3pkhQRlrR9kXkckLTzqM_3mwvNWjYqpn63UJkWGSsA
```

## Usage

Execute the ngrok.exe and type this command into the terminal that pops up to enable the reverse proxy.
```bash
ngrok http 80
```

Also start the API with running the main.py file

Afterwards set the webhook with running the webhook-setter.py in the webhook directory.

Chat with the bot :)

## Installation (aufsetzen mit docker)

Install docker if not already installed.

# If images (chatbot_telegram_api & webhook) are already available: 

Move into directory that contains the docker-compose.yml and start everything with.
```bash
docker compose up
```
# If images (chatbot_telegram_api & webhook) are not already available:

Move into directory ChatbotTelegramAPI/ and execute in terminal:

```bash
docker build -t chatbot_telegram_api:1.1 ./
```

Afterwards move into directory webhook/ and execute in terminal:

```bash
docker build -t webhook:1.0 ./
```

After building the images start everything with docker compose. Move into directory that contains the docker-compose.yml and start everything with.
```bash
docker compose up
```

Go to the Telegram page of the Chatbot (t.me/customer_support_chatbot) and chat with it :)

