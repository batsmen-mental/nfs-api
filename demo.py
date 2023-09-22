from flask import Blueprint, request
import mysql.connector
demo = Blueprint("demo", __name__)

@demo.route('/', methods=['POST', 'GET', 'DELETE'])
def main():

    Host = "nfi-demo-database.c2cn8z8gktfp.us-east-1.rds.amazonaws.com"
    Port = 3306
    User = "admin"
    Password = "nfiadminpwd1!"
    database = "demodb"
    query = "SELECT * FROM company"
    mydb = mysql.connector.connect(host=Host, user=User, port=Port, password=Password, database=database,
                                   charset='utf8')
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(query)
    if "SELECT" in query:
        results = mycursor.fetchall()
        mydb.commit()
        return (results, 500)
    else:
        mydb.commit()
        return ('Successful', 500)
    mydb.close()