from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error
#hello

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/coaches")
def coaches():
    return render_template("coaches.html")
    

@app.route("/fighter")
def fighter():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()

    mycursor.execute("SELECT * FROM Fighters")
    data = mycursor.fetchall()
    return render_template("fighter.html", data = data)

@app.route("/referee")
def referee():
    return render_template("referee.html")

@app.route("/sponsor")
def sponsor():
    
    return render_template("sponsor.html")

@app.route("/stadium")
def stadium():

    return render_template("stadium.html")

@app.route("/info")
def info():
    return render_template("info.html")
    

@app.route("/result",methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()
    name = output["name"]

    return render_template("index.html", name = name)

@app.route("/bestFighter",methods = ['POST', "GET"])
def bestFighter():
    results1 = request.form['fighter1']
    results2 = request.form['fighter2']
    print(results1,results2)
    database = r"boxing.sqlite"
    conn = openConnection(database)
    _conn = conn.cursor()
    sql = """
    SELECT f_name
    FROM(
        SELECT f_name, MAX(f_wins)
        FROM Fighters 
        WHERE f_name = ?
        OR f_name = ?
    )
    """
    args = [results1, results2]
    _conn.execute(sql,args)
    query = _conn.fetchall()
    print(query)

    _conn.execute("SELECT * FROM Fighters")
    data = _conn.fetchall()


    return render_template("fighter.html",fighter = query, data = data)

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def findFighter(_conn):
    c = _conn.cursor()
    sql = """
    SELECT f_name,max(f_wins)
    FROM Fighters
    JOIN Regions on f_cityKey = r_cityKey;
    """
    c.execute(sql)
    tuples = c.fetchall()
    for row in tuples:
        output = '{:>0}|{:>0}'.format(row[0],row[1])
        print(output)

    
def main():
    database = r"boxing.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        findFighter(conn)
        

    closeConnection(conn, database)

if __name__ == '__main__':
    main()
    app.run(debug= True)