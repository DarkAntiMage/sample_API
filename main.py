from flask import Flask, request, jsonify
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="28April3",
  database="api_db",
  auth_plugin='mysql_native_password'
)

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/yahahaha/', methods=['GET'])
def lah():
    return "yha gituuu"

@app.route('/users', methods=['POST'])
def create_user():
    data= request.get_json()

    mycursor = mydb.cursor()

    sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
    val = (str(data['name']), str(data['email']))
    mycursor.execute(sql, val)

    mydb.commit()
    return "berhasil"

@app.route('/users', methods=['GET'])
def tampil_db():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM user")

    myresult = mycursor.fetchall()
    return jsonify(myresult)

@app.route('/users/<id>', methods=['GET'])
def tampil_id(id):
    mycursor = mydb.cursor()

    mycursor.execute(f'SELECT * FROM user WHERE id={id}')

    myresult = mycursor.fetchall()
    return jsonify(myresult[0])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)