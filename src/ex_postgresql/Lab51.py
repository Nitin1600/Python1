# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
#
# print("Database connected sucessfully")import argparse


# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
#
# print("Database connected sucessfully")
#
# cur = conn.cursor()
# cur.execute("""CREATE TABLE COMPANY2
#             (ID INT PRIMARY KEY NOT NULL,
#             NAME TEXT NOT NULL,
#             AGE INT NOT NULL,
#             ADDRESS CHAR(50),
#             SALARY REAL);""")
#
# print("Table created sucessfully")
# conn.commit()
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
#
# print("Database connected sucessfully")

# cur = conn.cursor()
# cur.execute("INSERT INTO COMPANY2(ID,NAME,AGE,ADDRESS,SALARY)\
#     VALUES(1,'Paul',22,'California',20000)")
# cur.execute("INSERT INTO COMPANY2(ID,NAME,AGE,ADDRESS,SALARY)\
#     VALUES(2,'Tim',23,'Adelaide',12000)")
# cur.execute("INSERT INTO COMPANY2(ID,NAME,AGE,ADDRESS,SALARY)\
#     VALUES(3,'David',25,'Perth',50000)")
# cur.execute("INSERT INTO COMPANY2(ID,NAME,AGE,ADDRESS,SALARY)\
#     VALUES(4,'Rahul',23,'India',65000)")
#
# conn.commit()
# print("Inserted into table successfully")
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
#
# print("Database connected sucessfully")
#
# cur = conn.cursor()
# cur.execute("SELECT id,name,age,address,salary from Company2")
# rows = cur.fetchall()
# for row in rows:
#     print("id: ",row[0])
#     print("name: ",row[1])
#     print("age: ",row[2])
#     print("address: ",row[3])
#     print("salary: ", row[4], "\n")
#
# print("Operation done successfully")
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
#
# print("Database connected sucessfully")

# cur = conn.cursor()
# cur.execute("UPDATE COMPANY2 set SALARY = 12500.0 where ID=1")
# conn.commit()
# print("The updated row count is: ", cur.rowcount)
#
# cur.execute("SELECT id,name,age,address,salary from Company2")
# rows = cur.fetchall()
# for row in rows:
#     print("id: ", row[0])
#     print("name: ", row[1])
#     print("age: ", row[2])
#     print("address: ",row[3])
#     print("salary: ", row[4], "\n")
#
# print("Database updated successfully")
# conn.close()

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")

print("Database connected sucessfully")

cur = conn.cursor()
cur.execute("DELETE from COMPANY2 where id=3")
conn.commit()
print("Total number of row deleted are: ", cur.rowcount)

cur.execute("Select id,name,age,address,salary from Company2")
rows= cur.fetchall()
for row in rows:
    print("id: ", row[0])
    print("name: ", row[1])
    print("age: ", row[2])
    print("address: ",row[3])
    print("salary: ", row[4], "\n")

print("Database updated successfully")
conn.close()

