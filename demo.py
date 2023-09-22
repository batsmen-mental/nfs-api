import mysql.connector

def query_db(query):
    inspector_id = 1
    Host = "nfi-demo-database.c2cn8z8gktfp.us-east-1.rds.amazonaws.com"
    Port = 3306
    User = "admin"
    Password = "nfiadminpwd1!"
    database = "demodb"
    query = f"SELECT i.inspection_id, i.start_date, c.name  from inspections i, customer c  where i.customer_id = c.customer_id  AND inspector_id = {int(inspector_id)} and DATE_ADD(start_date , INTERVAL(-WEEKDAY(start_date)) DAY) = DATE_ADD(CURDATE() , INTERVAL(-WEEKDAY(CURDATE())) DAY);"
    mydb = mysql.connector.connect(host=Host, user=User, port=Port, password=Password, database=database,
                                   charset='utf8')
    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(query)
    if "SELECT" in query:
        results = mycursor.fetchall()
        mydb.commit()
        # return (str(results).replace('[','').replace('(','').replace(']','').replace('\'','').replace(' ','').replace(')',''), 500)
        return results
    else:
        mydb.commit()
        return ("Successful")
    mydb.close()