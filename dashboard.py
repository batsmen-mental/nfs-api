from flask import Blueprint, request
dashboard = Blueprint("dashboard", __name__)

@dashboard.route('/', methods=['POST', 'GET', 'DELETE'])
def main_dashboard():
    valid_username_list = ['inspector','company','owner','firemarshall']
    if request.method == "GET":
        try:
            username = request.args['username']
            try:
                if "inspector" in username:
                    response = '{"Week_Starting":"09/19/2023","JobList":[{"JobID":1964,"JobDate":"09/19/2023","Company":"Best Hospital"},{"JobID":1999,"JobDate":"09/22/2023","Company":"On Fire BBQ"}]}'
                return (response, 200)
            except:
                response = f"Invalid Username. Try one of the following: {valid_username_list}"
                return (response, 500)
        except Exception as e:
            response = "Error: " + str(e)
            return (response, 500)
    else:
        return ('<h2>ERROR. You must submit using "GET"<h2>', 500)