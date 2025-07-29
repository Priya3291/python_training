import mysql.connector

def insert_data(id, name, email):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='roottoor',
        database='priya_ece'
    )
    print("Connected to the database successfully")
    
    mycursor = mydb.cursor()
    sql = "INSERT INTO people (id, name, email) VALUES (%s, %s, %s)"
    val = (id, name, email)  # Tuple is preferred
    mycursor.execute(sql, val)
    
    print(mycursor.rowcount, "record inserted.")  # Print this before closing cursor
    
    mydb.commit()
    mycursor.close()
    mydb.close()

id = input("Enter the ID: ")
name = input("Enter the name: ")
mail = input("Enter the email: ")
insert_data(id, name, mail)