from flask import Blueprint, request, render_template
webpages = Blueprint("webpages", __name__)

@webpages.route('/add_customer', methods=['POST', 'GET', 'DELETE'])
def main_dashboard():
    return render_template('/webpages/add_customer.html')