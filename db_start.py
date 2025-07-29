class DbMethods:
    from db_config import getDb
    def insertData(id,name,email):
        mydb=getDb()
        mycursor=mydb.cursor()
        sql="INSERT INTO user1(id,name,email)VALUES(%s%s%s)"
        val=(id,name,email)
        mycursor.execute(sql,val)

        mydb.cursor()
        mycursor.close()
        mydb.close()
        print("data is inserted")
    