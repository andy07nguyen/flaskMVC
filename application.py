from flask import Flask, render_template, session, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'myfriends')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friend")
    print friends
    return render_template('index.html', friends=friends)


@app.route('/addFriend', methods = ['POST'])
def create():
    query = "INSERT INTO friend (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
