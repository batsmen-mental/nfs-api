from flask import Flask
application = Flask(__name__)

@application.route('/', methods=['GET'])
def index():
    return'Hello World'

@application.route('/users', methods=['GET'])
def users():
    import users
    users.main()