import json
import os

import websocket
from slacker import Slacker

import shorty

# BotUserOauth = os.environ["BOT_USER_OAUTH"]
token = os.getenv('SLCK_TOKEN')

slack = Slacker(token)
response = slack.rtm.start()
sock_endpoint = response.body['url']
ws = websocket.create_connection(sock_endpoint)


# websocket Processing Part
def run():
    while True:
        try:
            msg = json.loads(ws.recv())
            print(msg)
            if 'files' in msg.keys():
                print("사진입력!! 스킵~")
                continue
            if 'text' in msg.keys() and 'user' in msg.keys():
                # slack.chat.post_message(msg['channel'], msg['text'] + "의 날씨정보를 가져오고 있습니다. 잠시만 기다려 주세요..")
                result = shorty.wordpop(msg['text'])
                fin = ''.join(result)
                slack.chat.post_message(msg['channel'], fin)

        except websocket.WebSocketTimeoutException:
            ws.send(json.dumps({'type': 'ping'}))

        except websocket.WebSocketConnectionClosedException:
            print("Connection closed")

            return
        except Exception as e:
            print("error : ", e)

            return


# while True:
run()