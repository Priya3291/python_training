from flask import Flask,request,render_template,jsonify
from flask_mysqldb import MySQL

# Create object for Flask
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'priya_ece'
mysql = MySQL(app)


@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/myweb',methods=['GET'])
def myweb():
    return render_template("index.html")

@app.route('/myname')
def printmyname():
    return 'priya'
@app.route('/home')
def loadHomeHtml():
    return render_template("home.html")

@app.route('/about')
def loadaboutHtml():
    return render_template("home_about.html")

@app.route('/contact')
def loadcontactHtml():
    return render_template("hom_bc.html")

@app.route('/people_detail')
def peopleDetails():
    sql = "Select * from people"
    cur  = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return jsonify (results)

@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")

@app.route('/getDatainHtml')
def getDataInHtml():
    return render_template("register.html")
@app.route("/add", methods=['POST'])
def addpeople():
    email = request.form['email']
    password = request.form['password']
    id = request.form['id']
    
    cur = mysql.connection.cursor()
    sql = "INSERT INTO people (id, password, email) VALUES (%s, %s, %s)"
    val=[id, password, email]
    cur.execute(sql, (id, password, email))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Record added successfully!"})
#-------------------------------------------------------------------------------------------------------------------------------
@app.route("/update", methods=['POST'])
def updatepeople():
    id = request.form['id']
    email = request.form['email']
    cur = mysql.connection.cursor()
    sql = "update people set email = %s where id = %s"
    val=[email,id]
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()
    return "updated successfully"

@app.route("/delete", methods=['POST'])
def deletepeople():
    id = request.form['id']
    cur = mysql.connection.cursor()
    sql = "delete from people where id = %s"
    val=[id]
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()
    return "deleted successfully"
@app.route("/delete_form", methods=['GET'])
def delete_form():
    return render_template("delete.html")

if __name__ == '__main__' :
   app.run()