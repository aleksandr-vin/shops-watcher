#!/usr/bin/env bash

set -e

echo "Creating secret: telegram bot token"
echo -n ${TELEGRAM_BOT_TOKEN?} > $(pwd)/.SECRET.bot-token

kubectl create secret generic secrets \
	--namespace vrcover-shop-eu-scraper \
	--from-file=bot-token=$(pwd)/.SECRET.bot-token
