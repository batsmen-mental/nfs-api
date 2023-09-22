from flask import Blueprint, request
test = Blueprint("test", __name__)

@dashboard.route('/', methods=['GET')
def index()
    return ("Successful",200)
'''
def test_db():
    Host = "nfi-demo-database.c2cn8z8gktfp.us-east-1.rds.amazonaws.com"
    Port = 3306
    User = "admin"
    Password = "nfiadminpwd1!"
    database = "demodb"
    query = "select * from company"

    mydb = mysql.connector.connect(host=Host, user=User, port=Port, password=Password, database=database, charset='utf8')
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(query)
    results = mycursor.fetchall()
    mydb.commit()
    mydb.close()
    # return (str(results).replace('[','').replace('(','').replace(']','').replace('\'','').replace(' ','').replace(')',''),200)
    return (str(results),200)
'''