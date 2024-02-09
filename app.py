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
    commandd = open('commandList.txt', 'r')
    command_list = commandd.read()
    intro_text='Hi, my name is $$$$$$.\nI\'m a line-bot made for performing simple tricks.\nType in \'command\'to show how to use Toadog :)\nToadog is still very new, update will be performed in the near future.'
    highrand = 20

    message = text = event.message.text

    #20 dice show
    luckynumber = ""
    if message[0].isnumeric():
        fnum = int(message[0])
        if message[1] =='d':
            ttl=0
            luckynumber = ""
            for g in range(fnum):
                randnum = random.randint(1,highrand)
                luckynumber = luckynumber + str(randnum) + '\n'
                ttl = ttl + randnum
            no_leading_num_message = message[2:]
            luckynumber = luckynumber + '[' + no_leading_num_message.strip() + ']' 
            if fnum>1:
                luckynumber = luckynumber + '\n' + 'Ttl: ' + str(ttl) + '\n' + 'Avg: ' + str(ttl/fnum)
            line_bot_api.reply_message(event.reply_token,[TextSendMessage(luckynumber)])
    #character stat
    elif message.lower().find('d character ')==0:
        if len(message)>12:
            savings = message[12:].lsplit().rsplit()
            if len(savings)!=0:
                savings = savings.split(" ", 1)
                while savings(len(savings)-1).find(' ')!=-1:
                    savings = savings + savings(len(savings)-1).split(" ", 1)
                stat_output = "Name: " + savings[0] +'\n'
                for y in savings:
                    if y != savings[0]:
                        stat_output = stat_output + y + ': ' + random.randint(1,highrand) + '\n'
                line_bot_api.reply_message(event.reply_token,[TextSendMessage(stat_output)])
            else:
                line_bot_api.reply_message(event.reply_token,[TextSendMessage("P")])
        else:
            line_bot_api.reply_message(event.reply_token,[TextSendMessage("Please insert a name for your character ><")])
    #dice default
    elif message.lower().find('d ')==0:
        luckynumber = luckynumber + str(random.randint(0,20)) + '\n'
        no_leading_num_message = message[1:]
        luckynumber = luckynumber + '[' + no_leading_num_message.strip() + ']'
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(luckynumber)])
    #command list show
    if message.lower().find('command')==0:
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(command_list)])

    #introduction show
    elif message.find('intro')==0:
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text=intro_text, emojis=intro_emoji)])
    commandd.close()



    #auto reply 
    #line_bot_api.reply_message(event.reply_token,[TextSendMessage(message)])
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)