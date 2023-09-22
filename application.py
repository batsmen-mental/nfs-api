from flask import Flask
from users import users
from dashboard import dashboard
from demo import demo
application = Flask(__name__)

application.register_blueprint(users, url_prefix="/users")
application.register_blueprint(dashboard, url_prefix="/dashboard")
application.register_blueprint(demo, url_prefix="/demo")

@application.route('/', methods=['GET'])
def index():
    return'Hello World'

if __name__ == '__main__':
    application.run(debug=True)