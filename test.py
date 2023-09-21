import mysql.connector

Host = "database-2.czh8zvuvgqy8.us-east-1.rds.amazonaws.com"
Port = 3306
User = "admin"
Password = "Welcome123!"
database = "test"

mydb = mysql.connector.connect(host=Host, user=User, port=Port, password=Password, database=database, charset='utf8')
mycursor = mydb.cursor(buffered=True)
check_record_sql = "create table users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,username varchar(255),first_name varchar(255),last_name varchar(255), UNIQUE (username));"
#check_record_sql = "INSERT INTO users (username, first_name, last_name) VALUES ('test_user', 'Jim', 'Smith');"
#check_record_sql = "SELECT * FROM users;"
#check_record_sql = "desc users"
#insert into users (username, first_name, last_name) values ("test_user", "Jim", "Smith")"
mycursor.execute(check_record_sql)
results = mycursor.fetchall()
mydb.commit()

print(results)

'''
if 0 in results:
    post_to_facebook_group(response_type + "\n" + location)
    mycursor = mydb.cursor()
    sql = "INSERT INTO accidents (dispatch_call_datetime, location, response_type, call_status, agency, district_zone, status, record_key, last_updated) VALUES (\'" + dispatch_call_datetime + "\', \'" + location + "\', \'" + response_type + "\', \'" + call_status + "\', \'" + agency + "\', \'" + district_zone + "\', \'" + status + "\', \'" + key + "\', \'" + datetime_stamp + "\')"
    mycursor.execute(sql)
    mydb.commit()
else:
    ##Check to see if the call status as changed. If it did, post a update to the existing post##
    check_record_sql = "Select call_status from hcso_database.accidents where record_key = \"" + key + "\";"
    mycursor.execute(check_record_sql)
    results = str(mycursor.fetchone()).replace('\'', '').replace('(', '').replace(',)', '')
    mydb.commit()
    print(results)

    mycursor = mydb.cursor()
    sql = "UPDATE hcso_database.accidents SET dispatch_call_datetime = '" + dispatch_call_datetime + "', location =  '" + location + "', response_type = '" + response_type + "', call_status = '" + call_status + "', agency = '" + agency + "', district_zone = '" + district_zone + "', status = '" + status + "', last_updated = '" + datetime_stamp + "' WHERE record_key = '" + key + "'"
    mycursor.execute(sql)
    mydb.commit()
'''
mydb.close()