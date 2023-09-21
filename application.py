from flask import Flask
from users import users
application = Flask(__name__)

application.register_blueprint(users, url_prefix="/users")

@application.route('/', methods=['GET'])
def index():
    return'Hello World'

if __name__ == '__main__':
    application.run(debug=True, port=3999)