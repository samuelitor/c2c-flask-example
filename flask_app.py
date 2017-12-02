
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/bananas')
def hello_bananas():
    return 'Hello from Flask! Also, bananas!'
