from flask import Flask, request, json

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello World'


@application.route('/user', methods=['GET'])
def view_user():
    if request.method == 'GET':
        return "Hello, this is a test page."
