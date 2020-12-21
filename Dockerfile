FROM python:3

RUN python -m pip install --upgrade pip

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY vrcover-shop-eu-scraper.py /code

ENV TELEGRAM_BOT_TOKEN=PUT-YOUR-TELEGRAM-BOT-TOKEN-HERE
ENTRYPOINT ["python"]
CMD ["vrcover-shop-eu-scraper.py"]
