from flask import Blueprint, request
from db_actions import query_db
company = Blueprint("company", __name__)

@company.route('/add', methods=['POST', 'GET', 'DELETE'])
def add_company():
    if request.method == "POST":
        try:
            name = request.form.get('name',None)
            address = request.form.get('address',None)
            address2 = request.form.get('address2',None)
            city = request.form.get('city',None)
            state = request.form.get('state',None)
            zip = request.form.get('zip',None)
            county = request.form.get('county',None)
            phone = request.form.get('phone',None)
            phone2 = request.form.get('phone2',None)
            fax = request.form.get('fax',None)
            website = request.form.get('website',None)
            try:
                print(f"name: {name}")
                query = f"SELECT i.starting_week, i.inspection_id, i.start_date, c.name  from inspections i, customer c  where i.customer_id = c.customer_id  AND inspector_id = {userid} and starting_week = '{starting_week}';"
                response = query_db(query)
                return (response, 200)
            except:
                response = f"Invalid UserID."
                return (response, 500)
        except Exception as e:
            response = "Error: " + str(e)
            return (response, 500)
    else:
        return ('<h2>ERROR. You must submit using "GET"<h2>', 500)