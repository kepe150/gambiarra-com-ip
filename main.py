import urllib.request
import json
from discord_webhook import DiscordWebhook
import time
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

external_ip = 0
webhook_link = os.getenv('WEBHOOK_LINK')

print(webhook_link)

def get_external_ip():
  with urllib.request.urlopen('https://api.ipify.org?format=json') as response:
    data = json.load(response)
    return data['ip']

if __name__ == "__main__":
  while True:
    ip = get_external_ip()
    if ip != external_ip:
        webhook = DiscordWebhook(url=webhook_link,
         content=f"O ip mudou e é esse: {ip}.\n\n**VAI FAZER LOGO O SISTEMA DE DDNS COM O CLOUDFLARE SEU VAGABUNDO!**")
        response = webhook.execute()
        print(f"O ip mudou: {ip}")
        external_ip = ip
        time.sleep(60)



