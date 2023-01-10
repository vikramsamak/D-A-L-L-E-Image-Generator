from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flaskwebgui import FlaskUI
import openai

app = Flask(__name__)

openai.api_key = "YOUR-OPEANAI'S-API-KEY"

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/image_generator", methods=['GET'])
def image_generator():
    bot_input = request.args.get('botinput')
    imgsize = request.args.get('imgsize')
    response = openai.Image.create(
        prompt=bot_input,
        n=2,
        size=imgsize
    )
    
    image_url_1 = response['data'][0]['url']
    image_url_2 = response['data'][1]['url']
    urls={"url_1":image_url_1,"url_2":image_url_2}
    return urls

if __name__ == "__main__":
    app.run(debug=True)  # for debug
