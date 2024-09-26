# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import sys
import os

import logging
logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s - %(message)s', level=logging.INFO)

def telegramming(msg):
    from telegram import Bot
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    chat_id = 115668939 # my channel
    bot.send_message(chat_id=chat_id, text=msg)


logging.debug("Fetching page")
url = u"https://eu.vrcover.com/products/facial-interface-foam-replacement-set-for-oculus\u2122-quest-2-winter-edition"
response = requests.get(url)
logging.info(f"Page fetched {len(response.content)} bytes in {response.elapsed.total_seconds()} seconds")
soup = BeautifulSoup(response.text, "html.parser")
for l in soup.find_all('script', id="ProductJson-product"):
    product = json.loads(l.string)
    for v in product['variants']:
        logging.info(f"{v['sku']} {'available' if v['available'] else 'not-available'}: {v['name']}: {url}")
        if v['available']:
            logging.info("Product is available, telegramming")
            telegramming(f"{v['sku']} {'available' if v['available'] else 'not-available'}: {v['name']}: {url}")
        else:
            logging.info("Product is not available, not telegramming")
            telegramming("Just checking")
