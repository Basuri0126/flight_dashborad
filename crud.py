import mysql.connector

# connect to mysql

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Bh@t1yaa',
        port='3306',
        database='flight'
    )
    mycursor = conn.cursor()
    print('Connection established')
except:
    print("Connection error")

#  create database on server
# mycursor.execute('CREATE DATABASE flight')
# conn.commit()

# create table
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS airport(
        airport_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(40) NOT NULL,
        city VARCHAR(50) NOT NULL,
        code VARCHAR(50) NOT NULL)
""")

conn.commit()

# mycursor.execute('''
#   INSERT INTO airport VALUES
#   (1, 'IGIA', 'Dehli', 'DEH'),
#   (2, 'SBCA', 'Kolkata', 'CCU'),
#   (3, 'CSMA', 'Mumbai', 'BOM')
# ''')
# conn.commit()

# retrieve
mycursor.execute('SELECT * FROM airport WHERE airport_id>1')
data = mycursor.fetchall()
print(data)

# update
# mycursor.execute("""
# UPDATE airport
# SET name = 'Bombay'
# WHERE airport_id = 3
# """)
# conn.commit()

# delete
# mycursor.execute("""
#   DELETE FROM airport WHERE airport_id = 3
# """)
# conn.commit()

mycursor.execute('SELECT * FROM airport')
data = mycursor.fetchall()
print(data)