from flask import Blueprint, request, render_template
from db_actions import query_db
webpages = Blueprint("webpages", __name__)

@webpages.route('/add_customer', methods=['POST', 'GET', 'DELETE'])
def main():
    query = f"SELECT * FROM customer;"
    response = query_db(query)
    return (response, 200)
    # return render_template('webpages/add_customer.html', results=response)