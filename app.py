from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def root():
    #requests.post()
    return render_template('index.html' , arg1="arg1", arg2="arg2")

if __name__ == "__main__":
    app.run()