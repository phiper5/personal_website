#!/usr/bin/python3

from flask import Flask, render_template

# Create the application host
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
