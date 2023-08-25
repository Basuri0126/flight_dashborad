import mysql.connector
from mysql.connector import Error
import pandas as pd


class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                database='flight',
                port='3306',
                password='Bh@t1yaa',
                user='root'
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT DATABASE();")
            self.record = self.cursor.fetchone()
            print(f'Connection established with {self.record} database')
        except Error as e:
            print('Error with connected with database ', e)

    def fetch_city(self):
        city = []
        self.cursor.execute("""SELECT DISTINCT(source) FROM flight_data
                               UNION
                               SELECT DISTINCT(destination) FROM flight_data;""")
        data = self.cursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self, source, destination):
        self.cursor.execute(f"""
        SELECT airline, date_of_journey, 'dep_time', 'duration', 'price' FROM flight.flight_data 
        WHERE source='{source}' OR destination='{destination}';
        """)
        data = self.cursor.fetchall()
        return data

    def fetch_pie_data(self):
        airline = []
        count = []
        self.cursor.execute("""
        SELECT airline, COUNT(*) FROM flight.flight_data
        GROUP BY airline;
        """)
        data = self.cursor.fetchall()
        for item in data:
            airline.append(item[0])
            count.append(item[1])
        df = pd.DataFrame(list(zip(airline, count)), columns=['Airline', 'Count'])
        return df

    def fetch_busy_airport(self):
        airline = []
        count = []
        self.cursor.execute("""SELECT source, COUNT(*) FROM (SELECT source FROM flight_data
                                UNION ALL
                                SELECT destination FROM flight_data) t1
                                GROUP BY t1.source
                                ORDER BY COUNT(*) DESC;""")
        data = self.cursor.fetchall()
        for item in data:
            airline.append(item[0])
            count.append(item[1])
        df = pd.DataFrame(list(zip(airline, count)), columns=['Airline', 'Count'])
        return df

    def fetch_daily_flight(self):
        dates = []
        count = []
        self.cursor.execute("""
        SELECT date_of_journey, COUNT(*) FROM flight_data
        GROUP BY date_of_journey;
        """)
        data = self.cursor.fetchall()
        for item in data:
            dates.append(item[0])
            count.append(item[1])
        df = pd.DataFrame(list(zip(dates, count)), columns=['Date', 'No. of Flight'])
        return df






