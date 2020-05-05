import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="vn-gems", user='cwviet', password='viet8660', host='maindb.cexrfznwa2iv.ap-northeast-2.rds.amazonaws.com', port= '5432'
   #database="khanhtu", user='postgres', password='123456', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS sensorsdata2")

#Creating table as per requirement
# sql ='''CREATE TABLE devices
# (
#     id serial PRIMARY KEY NOT NULL,
#     deviceid integer NOT NULL,
#     mode boolean,
#     relay1 boolean,
#     relay2 boolean,
#     lowertemp real,
#     upperhumi integer,
#     uppertemp real,
#     lowerhumi integer
# )'''
sql ='''CREATE TABLE sensorsdata
(
    id serial PRIMARY KEY NOT NULL,
    deviceid integer NOT NULL,
    temp real,
    humi integer,
    light integer
)'''
cursor.execute(sql)
print("Table created successfully........")

#Closing the connection
conn.commit()
conn.close()