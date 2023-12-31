from flask import Blueprint, request
from db_actions import query_db
from datetime import date, timedelta
dashboard = Blueprint("dashboard", __name__)

@dashboard.route('/details', methods=['POST', 'GET', 'DELETE'])
def main_dashboard():
    today = date.today()
    start = today - timedelta(days=today.weekday())
    # end = start + timedelta(days=6)
    if request.method == "GET":
        try:
            userid = request.args.get('userid', None)
            demodata = request.args.get('demodata', None)
            starting_week = request.args.get('starting_week', start)
            try:
                if demodata:
                    response = '{"WeekInfo":[{"Week_Starting":"09/11/2023","JobList":[{"JobID":1911,"JobDate":"09/11/2023","Customer":"Crazy Nails"},{"JobID":1923,"JobDate":"09/12/2023","Customer":"Top Fashion"},{"JobID":1924,"JobDate":"09/13/2023","Customer":"LazerTag Empire"},{"JobID":1931,"JobDate":"09/15/2023","Customer":"Yummy Stuff"}]},{"Week_Starting":"09/18/2023","JobList":[{"JobID":1964,"JobDate":"09/18/2023","Customer":"Best Hospital"},{"JobID":1999,"JobDate":"09/21/2023","Customer":"On Fire BBQ"},{"JobID":1944,"JobDate":"09/22/2023","Customer":"Water Source LLC"}]}]}'
                    return (response, 200)
                elif userid is not None:
                    query = f"SELECT i.starting_week, i.inspection_id, i.start_date, c.name  from inspections i, customer c  where i.customer_id = c.customer_id  AND inspector_id = {userid} and starting_week = '{starting_week}';"
                    response = query_db(query)
                    return (response, 200)
                else:
                    response = 'No Demo or no User Data. Please get some help'
                    return (response, 200)
            except:
                response = f"Invalid UserID."
                return (response, 500)
        except Exception as e:
            response = "Error: " + str(e)
            return (response, 500)
    else:
        return ('<h2>ERROR. You must submit using "GET"<h2>', 500)