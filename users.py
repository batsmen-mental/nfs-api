from flask import Blueprint, request
users = Blueprint("users", __name__)

@users.route('/', methods=['POST', 'GET', 'DELETE'])
def users_profile():
    if request.method == "POST":
        try:
            username = request.json['username']
            first_name = request.json['first_name']
            last_name = request.json['last_name']
            try:
                results = create_user(username, first_name, last_name)
                response_temp = results.split(',')
                response = '{"action":"CREATE","userid":' + response_temp[0] + ',"username":"' + response_temp[1] + '","first_name":"' + response_temp[2] + '","last_name":"' + response_temp[3] + '"}'
                return (response, 200)
            except Exception as e:
                response = "Database Error: " + str(e)
                return (response, 500)
        except Exception as e:
            response = "You are missing the following value: " + str(e)
            return (response, 500)
    elif request.method == "GET":
        try:
            username = request.args['username']
            try:
                query = "SELECT * from users where username = '" + username + "';"
                results = run_query(query)
                response_temp = results.split(',')
                response = '{"action":"GET","userid":' + response_temp[0] + ',"username":"' + response_temp[1] + '","first_name":"' + response_temp[2] + '","last_name":"' + response_temp[3] + '"}'
                return (response, 200)
            except Exception as e:
                response = "Database Error: " + str(e)
                return (response, 500)
        except Exception as e:
            response = "You are missing the following value: " + str(e)
            return (response, 500)
    elif request.method == "DELETE":
        try:
            username = request.args['username']
            try:
                query = "SELECT * from users where username = '" + username + "';"
                results = run_query(query)
                response_temp = results.split(',')
                delete_user(username)
                response = '{"action":"DELETE","userid":' + response_temp[0] + ',"username":"' + response_temp[1] + '","first_name":"' + response_temp[2] + '","last_name":"' + response_temp[3] + '"}'
                return (response, 200)
            except Exception as e:
                response = "Database Error: " + str(e)
                return (response, 500)
        except Exception as e:
            response = "You are missing the following value: " + str(e)
            return (response, 500)

    else:
        return ('<h2>ERROR. You must submit using "POST"<h2>', 500)

def create_user(username,first_name,last_name):
    query = "INSERT INTO users (username, first_name, last_name) VALUES ('" + username + "', '" + first_name + "', '" + last_name + "');"
    run_query(query)
    query = "SELECT * from users where username = '" + username + "';"
    results = run_query(query)
    return str(results)

def run_query(query):
    import mysql.connector

    Host = "database-2.czh8zvuvgqy8.us-east-1.rds.amazonaws.com"
    Port = 3306
    User = "nfidbuser"
    Password = "nfidbuserpwd1"
    database = "test"

    mydb = mysql.connector.connect(host=Host, user=User, port=Port, password=Password, database=database, charset='utf8')
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(query)
    if "SELECT" in query:
        results = mycursor.fetchall()
        mydb.commit()
        return str(results).replace('[','').replace('(','').replace(']','').replace('\'','').replace(' ','').replace(')','')
    else:
        mydb.commit()
    mydb.close()

def delete_user(username):
    query = "DELETE FROM users where username = '" + username + "';"
    run_query(query)