from flask import Blueprint, request, render_template
from db_actions import query_db
webpages = Blueprint("webpages", __name__)

@webpages.route('/add_customer', methods=['POST', 'GET', 'DELETE'])
def add_customer():
    query = f"SELECT * FROM customer;"
    response = query_db(query)
    return render_template('webpages/add_customer.html', response=response)

@webpages.route('/add_company', methods=['POST', 'GET', 'DELETE'])
def add_company():
    query = f"SELECT * FROM company;"
    response = query_db(query)
    return render_template('webpages/add_company.html', response=response)