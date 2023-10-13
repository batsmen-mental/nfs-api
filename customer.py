from flask import Blueprint, request, redirect
from db_actions import query_db
from config import format_json_response
customer = Blueprint("customer", __name__)

@customer.route('/add', methods=['POST'])
def add_customer():
    if request.method == "POST":
        try:
            name = request.form.get('name',None)
            address = request.form.get('address',None)
            address2 = request.form.get('address2','')
            city = request.form.get('city',None)
            state = request.form.get('state',None)
            zip = request.form.get('zip',None)
            county = request.form.get('county',None)
            phone = request.form.get('phone',None)
            phone2 = request.form.get('phone2','')
            fax = request.form.get('fax','')
            website = request.form.get('website','')

            #Return error is missing mandatory fields
            if None in (name, address, city, state, zip, county, phone):
                return(f"One or more required parameters are missing (name,address,city,state,zip,county,phone)",428)

            try:
                query = f"INSERT into customer (name,address,address2,city,state,zip,county,phone,phone2,fax,website) VALUES('{name}','{address}','{address2}','{city}','{state}','{zip}','{county}','{phone}','{phone2}','{fax}','{website}');"
                response = query_db(query)
                try:
                    if request.referrer:
                        return redirect (request.referrer)
                except:
                    return (response,200)
            except:
                response = f"Database Error."
                return (response, 520)
        except Exception as e:
            response = f"Error: {str(e)}"
            return (response, 520)
    else:
        return ('<h2>ERROR. You must submit using "POST"<h2>', 500)

@customer.route('/get', methods=['GET'])
def get_customer():
    if request.method == "GET":
        try:
            customer_id = request.args['customer_id']
        except:
            response = f"Invalid parmeter. Please pass a 'customer_id' parameter"
            return (response, 520)
        try:
            query = f"SELECT * FROM customer WHERE customer_id = {customer_id};"
            response = query_db(query)
            try:
                if request.referrer:
                    return redirect (request.referrer)
            except:
                return (response,200)
            return (format_json_response(200,1.03254747,response,[]), 200)
        except:
            response = f"Database Error."
            return (response, 520)
    else:
        return ('<h2>ERROR. You must submit using "GET"<h2>', 500)