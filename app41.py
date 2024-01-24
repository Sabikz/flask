from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

Message = namedtuple("Message", "text tag")
messages = []

#in terminal flask --app .\app41.py run
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', message=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    messages.append(Message(text, tag))
    return redirect(url_for('main'))

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

