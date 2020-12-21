# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import sys
import os

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

url = u"https://eu.vrcover.com/products/facial-interface-foam-replacement-set-for-oculus\u2122-quest-2-winter-edition"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup)
for l in soup.find_all('script', id="ProductJson-product"):

    #from telegram.ext import Updater
    #updater = Updater(token=os.getenv('VRCoverAvailabilityBot_TOKEN'), use_context=True)
    #dispatcher = updater.dispatcher

    # def start(update, context):
    #     print(update.effective_chat.id)
    #     context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    # from telegram.ext import CommandHandler
    # start_handler = CommandHandler('start', start)
    # dispatcher.add_handler(start_handler)
    # updater.start_polling()
    # updater.idle()

    from telegram import Bot
    bot = Bot(token=os.getenv('VRCoverAvailabilityBot_TOKEN'))
    chat_id = 115668939 # my channel

    product = json.loads(l.string)
    for v in product['variants']:
        print(f"{v['sku']} {'available' if v['available'] else 'not-available'}: {v['name']}: {url}", file = sys.stdout if v['available'] else sys.stderr)
        if v['available']:
            bot.send_message(chat_id=chat_id, text=f"{v['sku']} {'available' if v['available'] else 'not-available'}: {v['name']}: {url}")
