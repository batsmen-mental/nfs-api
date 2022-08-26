from flask import Flask, request, json

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello World'