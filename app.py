from libs import lib
from libs import prconfig
import json

from flask import Flask, request, abort, render_template

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, send_messages
)
from linebot.models.flex_message import BubbleContainer
from linebot.models.responses import BroadcastResponse

app = Flask(__name__)
app.config["DEBUG"] = True

line_bot_api = LineBotApi(prconfig.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(prconfig.CHANNEL_SECRET)

@app.route('/')
def root():
    print("##### root access.")
    print("### CHANNEL_ACCESS_TOKEN=" + prconfig.CHANNEL_ACCESS_TOKEN)
    print("### CHANNEL_SECRET=" + prconfig.CHANNEL_SECRET)

    # filedata = open('static\\json\\recipes.json','r', encoding="utf-8") # Windows Local.
    filedata = open('static/json/recipes.json','r', encoding="utf-8")
    jsondata = json.load(filedata)
    # line_bot_api.broadcast( FlexSendMessage (alt_text='Share recipe of daily life',contents=jsondata) )

    return render_template('index.html' , arg1=lib.TEST, arg2="root access.")

@app.route('/postmessage', methods=['POST'])
def postmessage():
    print ("##### postmessage access.")
    signature = request.headers['X-Line-Signature']
    print("### X-Line-Signature=" + signature)

    body = request.get_data(as_text=True)
    print("### body=" + body)

    json_body = request.get_json()
    replydestination = json_body['destination']
    replystr = json_body['events'][0]['message']['text']

    print("### replydestination=" + replydestination)
    print("### replystr=" + replystr)
    #line_bot_api.push_message(replydestination, TextMessage(replystr))

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("##### Invalid signature error.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("###### event.message.text=" + event.message.text)
    if event.message.text == "検索":
        print("##### in 検索")
        filedata = open('static/json/recipes.json','r', encoding="utf-8")
        jsondata = json.load(filedata)
        line_bot_api.reply_message(event.reply_token, FlexSendMessage (alt_text='Share recipe of daily life',contents=jsondata))

    elif event.message.text == "maintenance":
        print("##### in maintenance")
        line_bot_api.reply_message(event.reply_token, TextSendMessage("空気清浄機のメンテナンスですね。"))

    elif event.message.text == "toilet":
        print("##### in toilet")
        line_bot_api.reply_message(event.reply_token, TextSendMessage("シートでトイレ掃除ですね。"))

    elif event.message.text == "passport":
        print("##### in passport")
        line_bot_api.reply_message(event.reply_token, TextSendMessage("パスポート更新準備ですね。"))

    elif event.message.text == "license":
        print("##### in license")
        line_bot_api.reply_message(event.reply_token, TextSendMessage("免許更新の準備ですね。"))

    else:
        print("##### in else")
        line_bot_api.reply_message(event.reply_token, TextSendMessage("すみません、よくわかりません。"))
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(debug=True)
