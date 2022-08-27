from flask import Flask
application = Flask(__name__)

@application.route('/', methods=['GET'])
def index():
    return'Hello World'

@application.route('/user', methods=['GET'])
def user():
    return ('{"userid":"123","username":"testuser","first_name":"Jim","last_name":"Smith"}',400)