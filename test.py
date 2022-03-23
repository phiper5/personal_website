#!/usr/bin/python3

from flask import Flask, render_template

# Create the application host
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
