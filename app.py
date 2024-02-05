from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import random

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    intro_emoji = [
    {
        "index": 15,
        "productId": "5ac21a8c040ab15980c9b43f",
        "emojiId": "020"
    },
    {
        "index": 16,
        "productId": "5ac21a8c040ab15980c9b43f",
        "emojiId": "041"
    }
    ,
    {
        "index": 17,
        "productId": "5ac21a8c040ab15980c9b43f",
        "emojiId": "027"
    }
    ,
    {
        "index": 18,
        "productId": "5ac21a8c040ab15980c9b43f",
        "emojiId": "030"
    }
    ,
    {
        "index": 19,
        "productId": "5ac21a8c040ab15980c9b43f",
        "emojiId": "041"
    },
    {
        "index": 20,
        "productId": "5ac21a8c040ab15980c9b43f",
        "emojiId": "033"
    }
]
    f = open('commandList.txt', 'r')
    command_list = f.read()
    intro_text='Hi, my name is $$$$$$.\nI\'m a line-bot made for performing simple tricks.\nType in \'command\'to show how to use Toadog :)\nToadog is still very new, update will be performed in the near future.'
    message = text = event.message.text
    if message.find('d')==0:
        luckynumber = str(random.randint(0,20))
        if len(message)>2:
            luckynumber = luckynumber + " " + message[1:]
            luckynumber = luckynumber.strip()
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(luckynumber)])
    elif message.find('command')==0:
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(command_list)])
    elif message.find('intro')==0:
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text=intro_text, emojis=intro_emoji)])
    f.close()

    #auto reply #line_bot_api.reply_message(event.reply_token,[TextSendMessage(message)])
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)