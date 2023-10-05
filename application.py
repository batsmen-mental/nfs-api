from flask import Flask, render_template
from users import users
from dashboard import dashboard
from company import company
from customer import customer
application = Flask(__name__)

application.register_blueprint(users, url_prefix="/users")
application.register_blueprint(dashboard, url_prefix="/dashboard")
application.register_blueprint(company, url_prefix="/company")
application.register_blueprint(customer, url_prefix="/customer")

@application.route('/', methods=['GET'])
def index():
    return'Hello World'

@app.route('/admin')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(debug=True)