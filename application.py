from flask import Flask
from users import users
from dashboard import dashboard
from test import test
application = Flask(__name__)

application.register_blueprint(users, url_prefix="/users")
application.register_blueprint(dashboard, url_prefix="/dashboard")
application.register_blueprint(test, url_prefix="/test")

@application.route('/', methods=['GET'])
def index():
    return'Hello World'

if __name__ == '__main__':
    application.run(debug=True)