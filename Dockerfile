FROM ubuntu:latest

RUN mkdir -p /usr/src/slackbot-shorty
WORKDIR /usr/src/slackbot-shorty
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install python3-pip git build-essential
RUN ./mecab.sh
RUN pip3 install --no-cache-dir --requirement requirement.txt

COPY . .
CMD ["python3", "./slackbot.py"]