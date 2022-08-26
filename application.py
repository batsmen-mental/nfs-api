from flask import Flask, request, json

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello World'

'''
@application.route('/user', methods=['GET', 'POST'])
def view_user():
    if request.method == 'GET':
        return "Hello, I dont know what your name is"
    if request.method == 'POST':
        return json.dumps({'name': request.form['name']})
'''


@application.route('/user', methods=['POST'])
def view_user():
    return json.dumps({'name': request.form['name']})
