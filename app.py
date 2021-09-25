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

line_bot_api = LineBotApi(prconfig.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(prconfig.CHANNEL_SECRET)

@app.route('/')
def root():
    filedata = open('static/json/recipes.json','r', encoding="utf-8")
    jsondata = json.load(filedata)
    line_bot_api.broadcast( FlexSendMessage (alt_text='Share recipe of daily life',contents=jsondata) )

    return render_template('index.html' , arg1=lib.TEST, arg2="arg2")

if __name__ == "__main__":
    print(prconfig.CHANNEL_ACCESS_TOKEN)
    print(prconfig.CHANNEL_SECRET)
    app.run(debug=True)
