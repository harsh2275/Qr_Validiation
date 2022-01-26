from wsgiref import validate
import mysql.connector
from datetime import date
from datetime import datetime , timedelta
import datetime

def validiate(lis):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='try',
                                            user='root',
                                            password='855fc1@NOV25')
        cursor = connection.cursor()
        today = date.today()
        time = datetime.datetime.now()
        sql_select_query = "select * from main where HashValue = '{}'".format(lis)            
        cursor.execute(sql_select_query)
        record = cursor.fetchone()
        print(record)
        #print(record[5])
        now = datetime.datetime.now()
        tommy = now + datetime.timedelta(0,60)
    
    # Update single record now
        if record[4] == today :  
            sql_update_query = "Update main set Validate = 'Yes' where HashValue = '{}'".format(lis)
            cursor.execute(sql_update_query)
            connection.commit()
            return("Allowed")

        elif record[4] > today :  
            return("Arrive on ",record[4])
        
        else :
            sql_update_query = "Update main set Validate = 'No' where HashValue = '{}'".format(lis)
            cursor.execute(sql_update_query)
            connection.commit()
            return("You are Late")

    except mysql.connector.Error as error:
        print("Qr does not belong to hyperloops")
        print("Failed to update table record: {}".format(error))
        
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

#validiate("Harsh_20_2022-01-2618:48_2022-01-26 16:46:40.188936_harsh.agrawal2275@gmail.com")
#data=cursor.fetchall()
#count=cursor.rowcount
