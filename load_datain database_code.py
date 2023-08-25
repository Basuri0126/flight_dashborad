import mysql.connector
from mysql.connector import Error
import pandas as pd


try:
    conn = mysql.connector.connect(
        username='root',
        password='Bh@t1yaa',
        port='3306',
        database='flight',
        host='localhost',
    )
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f'connection established with {record}" database')
        cursor.execute("""DROP TABLE IF EXISTS flight_data;""")
        print("creating table----------")
        cursor.execute("""CREATE TABLE flight_data(
                airline VARCHAR(255), 
                date_of_journey DATE,
                source VARCHAR(255),
                destination VARCHAR(255),
                route VARCHAR(255),
                dep_time TIME,
                duration VARCHAR(255),
                total_stops VARCHAR(255),
                price INTEGER
                 )""")
        print('Table is created--------')

        csv_data = pd.read_csv('flights_cleaned - flights_cleaned.csv').fillna('NULL')

        for index, row in csv_data.iterrows():
            sql = """INSERT INTO flight_data(
                    airline, date_of_journey, source, destination, route, dep_time, duration, total_stops, price
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            data = (row['Airline'], row['Date_of_Journey'], row['Source'], row['Destination'], row['Route'],
                    row['Dep_Time'], row['Duration'], row['Total_Stops'], row['Price'])
            cursor.execute(sql, data)
            conn.commit()

except Error as e:
    print('Error while connecting to database', e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Mysql connection is closed")