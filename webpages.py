from flask import Blueprint, request, render_template
from db_actions import query_db
webpages = Blueprint("webpages", __name__)

@webpages.route('/add_customer', methods=['POST', 'GET', 'DELETE'])
def main():
    query = f"SELECT * FROM customer;"
    response = query_db(query)
    response = [{ "News" : "ABC", "Link" : "http://exampleabc.com", "Date": "01/03/20" },
           { "News" : "DEF", "Link" : "http://exampledef.com", "Date": "02/03/20" },
           { "News" : "GHI", "Link" : "http://exampleghi.com", "Date": "03/03/20" }]
    # return (response, 200)
    return render_template('webpages/add_customer.html', results=response)