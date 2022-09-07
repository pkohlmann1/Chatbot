import requests
import time

time.sleep(60)
NGROK_API_TOKEN = "2ERuqnMDsYZMzhptFAlEJyTcokr_44Jaa8ZCgjUJuU9g4u942"

CHATBOT_TOKEN = "5465490826:AAHGe7Q76oXE0STS7QGoWUra5t1CQbuybgw"

url = f'https://api.ngrok.com/tunnels'
headers = {"Authorization": "Bearer " + NGROK_API_TOKEN, "Ngrok-Version": "2"}
res = requests.get(url, headers=headers).json()

tunnel_https = next(filter(lambda tunnel: tunnel['proto'] == "https", res['tunnels']))
NGROK_HTTPS_URL = tunnel_https['public_url']

url = f'https://api.telegram.org/bot' + CHATBOT_TOKEN + '/setWebhook?url=' + NGROK_HTTPS_URL

res = requests.get(url)
