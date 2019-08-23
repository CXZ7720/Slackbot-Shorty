import json

import websocket
from slacker import Slacker

import shorty

# BotUserOauth = os.environ["BOT_USER_OAUTH"]
token = 'xoxb-392235298884-732535143956-tooz5FY3VSP2XIX1fAuIkBua'  # TEST workspace
# token = os.getenv('SLCK_TOKEN')

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
                result = shorty.validate(msg['text'])
                if result[0] == "PASS":
                    if result[1] == "ONEWORD":
                        print("1개 단어 입력은 건너뜀.")
                        continue
                    else:
                        print("도배방지 활성화 - 명사+동사 : ", result[1], "전체 형태소 : ", result[2])
                        continue
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
