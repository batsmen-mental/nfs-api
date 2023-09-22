from flask import Blueprint, request
import mysql.connector
dashboard = Blueprint("dashboard", __name__)

@dashboard.route('/', methods=['POST', 'GET', 'DELETE'])
def main_dashboard():
    valid_username_list = ['inspector','company','owner','firemarshall']
    if request.method == "GET":
        try:
            userid = request.args.get('userid', None)
            demodata = request.args.get('demodata', None)
            try:
                if demodata:
                    response = '{"WeekInfo":[{"Week_Starting":"09/11/2023","JobList":[{"JobID":1911,"JobDate":"09/11/2023","Customer":"Crazy Nails"},{"JobID":1923,"JobDate":"09/12/2023","Customer":"Top Fashion"},{"JobID":1924,"JobDate":"09/13/2023","Customer":"LazerTag Empire"},{"JobID":1931,"JobDate":"09/15/2023","Customer":"Yummy Stuff"}]},{"Week_Starting":"09/18/2023","JobList":[{"JobID":1964,"JobDate":"09/18/2023","Customer":"Best Hospital"},{"JobID":1999,"JobDate":"09/21/2023","Customer":"On Fire BBQ"},{"JobID":1944,"JobDate":"09/22/2023","Customer":"Water Source LLC"}]}]}'
                    return (response, 200)
                elif userid is not None:
                    query = f"SELECT i.inspection_id, i.start_date, c.name  from inspections i, customer c  where i.customer_id = c.customer_id  AND inspector_id = {int(userid)} and DATE_ADD(start_date , INTERVAL(-WEEKDAY(start_date)) DAY) = DATE_ADD(CURDATE() , INTERVAL(-WEEKDAY(CURDATE())) DAY);"
                    response = query_db(query)
                    return (response, 200)
                else:
                    response = 'No Demo or no User Data'
                    return (response, 200)
            except:
                response = f"Invalid UserID."
                return (response, 500)
        except Exception as e:
            response = "Error: " + str(e)
            return (response, 500)
    else:
        return ('<h2>ERROR. You must submit using "GET"<h2>', 500)

def query_db(query):
    Host = "nfi-demo-database.c2cn8z8gktfp.us-east-1.rds.amazonaws.com"
    Port = 3306
    User = "admin"
    Password = "nfiadminpwd1!"
    database = "demodb"
    mydb = mysql.connector.connect(host=Host, user=User, port=Port, password=Password, database=database,
                                   charset='utf8')
    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(query)
    if "SELECT" in query:
        results = mycursor.fetchall()
        mydb.commit()

        # return (str(results).replace('[','').replace('(','').replace(']','').replace('\'','').replace(' ','').replace(')',''), 500)
        return (results, 500)
    else:
        mydb.commit()
        return ('Successful', 500)
    mydb.close()