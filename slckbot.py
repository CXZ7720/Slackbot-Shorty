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
            if 'text' in msg.keys() and 'user' in msg.keys():
                # slack.chat.post_message(msg['channel'], msg['text'] + "의 날씨정보를 가져오고 있습니다. 잠시만 기다려 주세요..")
                result = shorty.wordpop(msg['text'])
                fin = ''.join(result)
                slack.chat.post_message(msg['channel'], fin)
                # break
                # return
        except websocket.WebSocketTimeoutException:
            ws.send(json.dumps({'type': 'ping'}))

        except websocket.WebSocketConnectionClosedException:
            print("Connection closed")
            # break
            return
        except Exception as e:
            print("error : ", e)
            # break
            return


# while True:
run()


# async def execute_bot():
#     ws = await websockets.connect(sock_endpoint)
#     while True:
#         message_json = json.loads(await ws.recv())
#         # print(message_json['type'])
#         if 'content' in message_json:
#             input_message = message_json['content']
#             print(input_message)
#             slack.chat.post_message(message_json['channel'],input_message)
#             continue
#         else:
#             print(message_json)
#
#
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# asyncio.get_event_loop().run_until_complete(execute_bot())
# asyncio.get_event_loop().run_forever()


def slack_notify(text=None, channel='random', username="Weatherpidia", attachments=None):
    slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)
