FROM python:3

RUN mkdir -p /usr/src/slackbot-shorty
WORKDIR /usr/src/slackbot-shorty

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --requirement requirements.txt

COPY . .
CMD ["python3", "./slackbot.py"]