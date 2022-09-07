# Chatbot-Telegram-API

This is the Chatbot-Telegram-API. This needs to run for being able to chat with the Telegram-Bot.
The Bots Telegram name is CustomerSupportChatbot (@customer_support_chatbot)

The Bots API-Token is 5465490826:AAHGe7Q76oXE0STS7QGoWUra5t1CQbuybgw

## Installation

Install required packages
```bash
pip install -r requirements.txt
```

Make sure you have all necessary model files for the self-trained model in the model directory. Otherwise use a pre-trained model.
The folder structure should look like this
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
ngrok http 5000
```

Also start the API with running the main.py file

Go to the Telegram page of the Chatbot (t.me/customer_support_chatbot) and chat with it :)
