#!/usr/bin/python3

from flask import Flask

# Create the application host
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
