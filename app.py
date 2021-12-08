from flask import Flask, render_template, request, url_for
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
    

@app.route("/result",methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()
    name = output["name"]

    return render_template("index.html", name = name)


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
    JOIN Regions on f_cityKey = r_cityKey
    WHERE r_country != 'USA';
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