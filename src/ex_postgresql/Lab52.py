# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
#
# print("Database connected successfully")
#
# cur = conn.cursor()
# cur.execute("""CREATE TABLE COMPANY3
#             (ID INT PRIMARY KEY NOT NULL,
#             NAME TEXT NOT NULL,
#             AGE INT NOT NULL,
#             ADDRESS CHAR(50),
#             SALARY REAL);""")
#
# conn.commit()
# conn.close()

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")

print("Database connected successfully")

cur = conn.cursor()
# cur.execute("INSERT into COMPANY3(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(1,'Amith',31,'Rajasthan',10000)")
# cur.execute("INSERT into COMPANY3(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(2,'Bomma',33,'MP',11000)")
# cur.execute("INSERT into COMPANY3(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(3,'Manav',32,'Gj',12000)")
# cur.execute("INSERT into COMPANY3(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(4,'Adithya',35,'AP',15000)")

# cur.execute("UPDATE COMPANY3 set SALARY=16000 where id=4")
# conn.commit()
# print("Total number of rows: ", cur.rowcount)

# cur.execute("SELECT id,name,age,address,salary from company3")
# rows = cur.fetchall()
# for row in rows:
#     print("id: ",row[0])
#     print("name: ",row[1])
#     print("age: ",row[2])
#     print("address: ",row[3])
#     print("salary: ",row[4],"\n")
#
# print("Selected successfully")
# conn.close()

cur.execute("DELETE from company3 where id=2")
conn.commit()
print("Total number of rows deleted: ", cur.rowcount)

cur.execute("SELECT id,name,age,address,salary from company3")
rows = cur.fetchall()
for row in rows:
    print("id: ",row[0])
    print("name: ",row[1])
    print("age: ",row[2])
    print("address: ",row[3])
    print("salary: ",row[4],"\n")

conn.commit()
conn.close()
