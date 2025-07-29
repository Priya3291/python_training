import mysql.connector
def email_exits(email):
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='roottoor',
        database='navya_cse'
        )
    mycursor=mydb.cursor()
    mycursor.execute(("SELECT count(id)as count FROM user1 where email=%s",(email)))
    myresult=mycursor.fetchall()
    print(myresult)
    if myresult[0][0]>=1:
        print("Email already exists")
    else:
        print("Emaildoes not exists")
        mycursor.close()
        mydb.close()
input_email=input("Enter the email to check:")
check_email_exists(input_email)    