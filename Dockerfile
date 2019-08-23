FROM python:3

RUN mkdir -p /usr/src/slackbot-shorty
WORKDIR /usr/src/slackbot-shorty
RUN bash <(curl -s https://raw.githubusercontent.com/koshort/peunjeon/master/scripts/mecab.sh)
COPY requirements.txt ./
RUN pip3 install --no-cache-dir --requirement requirements.txt

COPY . .
CMD ["python3", "./slckbot.py"]