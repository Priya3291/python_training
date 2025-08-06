import  sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("INSERT INTO user(name,age)VALUES(?,?)",("Alice",25))
cursor.execute("INSERT INTO user(name,age)VALUES(?,?)",("Alice",25))
conn.connect()
conn.close()