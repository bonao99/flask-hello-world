# https://code.visualstudio.com/docs/python/tutorial-flask
# python -m flask run --host=0.0.0.0 --port=8484
# docker run -p 8484:8484 -d flask-hello-world

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask app!'

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8484)