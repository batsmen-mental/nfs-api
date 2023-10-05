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
                query = f"INSERT into company (name,address,address2,city,state,zip,county,phone,phone2,fax,website) VALUES('{name}','{address}','{address2}','{city}','{state}','{zip}','{county}','{phone}','{phone2}','{fax}','{website}');"
                response = query_db(query)
                return (response, 200)
            except:
                response = f"Invalid UserID."
                return (response, 500)
        except Exception as e:
            response = "Error: " + str(e)
            return (response, 500)
    else:
        return ('<h2>ERROR. You must submit using "POST"<h2>', 500)