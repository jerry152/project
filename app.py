from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error
#hello

app = Flask(__name__)

#ROUTING FOR HOME PAGE
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result",methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()
    name = output["name"]
    return render_template("index.html", name = name)



#ROUTING FOR COACHES
@app.route("/coaches")
def coaches():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT * FROM Coaches")
    data = mycursor.fetchall()
    return render_template("coaches.html", data = data)

# choose coach the show there fighters 
@app.route("/trainedFighters",methods = ['POST', "GET"])
def trainedFighters():
    results1 = request.form['coaches1']
    print(results1)
    database = r"boxing.sqlite"
    conn = openConnection(database)
    _conn = conn.cursor()
    sql = """ 
SELECT f_name
FROM Fighters, Coaches
WHERE c_name = ?
and f_coachName = c_name;
    """
    args = [results1]
    _conn.execute(sql,args)
    query = _conn.fetchall()
    print(query)
    _conn.execute("SELECT * FROM Coaches")
    data = _conn.fetchall()


    return render_template("coaches.html",fighter = query, data = data, name = results1)
#where are the coaches from
@app.route("/coachesCity",methods = ['POST', "GET"])
def coachesCity():
    results2 = request.form['coaches2']
    print(results2)
    database = r"boxing.sqlite"
    conn = openConnection(database)
    _conn = conn.cursor()
    sql = """ 
SELECT r_name, r_state, r_country
FROM  Coaches, Regions
WHERE c_name = ?
and c_citykey = r_cityKey;
    """
    args = [results2]
    _conn.execute(sql,args)
    query = _conn.fetchall()
    print(query)
    _conn.execute("SELECT * FROM Coaches")
    data = _conn.fetchall()


    return render_template("coaches.html",city = query, data = data, name = results2)
    


#ROUTING FOR FIGHTERS
@app.route("/fighter")
def fighter():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT * FROM Fighters")
    data = mycursor.fetchall()
    return render_template("fighter.html", data = data)
    
@app.route("/bestFighter",methods = ['POST', "GET"])
def bestFighter():
    results1 = request.form['fighter1']
    results2 = request.form['fighter2']
    print(results1,results2)
    database = r"boxing.sqlite"
    conn = openConnection(database)
    _conn = conn.cursor()
    sql = """
    SELECT f_name, f_wins, f_losses, f_ties
    FROM(
        SELECT f_name, MAX(f_wins), f_wins, f_losses, f_ties
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


    return render_template("fighter.html",fighter = query[0], data = data)
#fighter record
@app.route("/fighterRec",methods = ['POST', "GET"])
def fighterRec():
    results3 = request.form['fighter3']
    print(results3)
    database = r"boxing.sqlite"
    conn = openConnection(database)
    _conn = conn.cursor()
    sql = """ 
SELECT *
FROM Fighters
Where f_name = ?
    """
    args = [results3]
    _conn.execute(sql,args)
    query = _conn.fetchall()
    print(query)
    _conn.execute("SELECT * FROM Fighters")
    data = _conn.fetchall()


    return render_template("fighter.html",Rec = query, data = data, name = results3)
    

#ROUTING FOR REFEREES
@app.route("/referee")
def referee():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT * FROM Referee")
    data = mycursor.fetchall()
    return render_template("referee.html", data = data)

@app.route("/cityRef", methods = ['POST', "GET"])
def cityRef():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT * FROM Referee")
    data = mycursor.fetchall()
    results1 = request.form['state1']
    sql = """
    SELECT rf_name, r_name, r_state
    FROM Referee
    JOIN Regions on rf_cityKey = r_cityKey
    WHERE r_state = ?
    """
    args = [results1]
    mycursor.execute(sql,args)
    info = mycursor.fetchall()
    return render_template("referee.html", data = data, answer = info)

@app.route("/mostRef", methods = ['POST', "GET"])
def mostRef():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT * FROM Referee")
    data = mycursor.fetchall()
    results1 = request.form['stadium']
    sql = """
    SELECT rf_name
    FROM Referee
    JOIN Regions on rf_cityKey = r_cityKey
    JOIN Stadium on r_cityKey = st_cityKey
    WHERE st_name = ?
    """
    args = [results1]
    mycursor.execute(sql,args)
    info = mycursor.fetchall()
    return render_template("referee.html", data = data, info = info)



#ROUTING FOR SPONSOR PAGE
@app.route("/sponsor")
def sponsor():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT s_name FROM Sponsors")
    data = mycursor.fetchall()

    return render_template("sponsor.html", data = data)

@app.route("/sponsorQ",methods = ['POST', "GET"])
def sponsorQ():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT s_name FROM Sponsors")
    data = mycursor.fetchall()
    results1 = request.form['sponsor1']
    sql = """
    SELECT f_name, r_country
    FROM Sponsors
    JOIN SponsoredFighter on s_sponsorKey = sp_sponsorKey
    JOIN Fighters on sp_fighterKey = f_fighterKey
    JOIN Regions on f_cityKey = r_cityKey
    WHERE s_name = ?
    """
    args = [results1]
    mycursor.execute(sql,args)
    data1 = mycursor.fetchall()
    print(data1)
    return render_template("sponsor.html", data = data, sponsor = results1,list = data1)



#ROUTING FOR STADIUM PAGE
@app.route("/stadium")
def stadium():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT * FROM Stadium")
    data = mycursor.fetchall()
    return render_template("stadium.html", data = data)

@app.route("/largestStadium",methods = ['POST',"GET"])
def largestStadium():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT * FROM Stadium")
    data = mycursor.fetchall()
    results1 = request.form['state1']
    sql = """
    SELECT st_name, MAX(st_size), st_maxpeople
    FROM Stadium
    JOIN Regions on st_cityKey = r_cityKey
    WHERE r_state = ?
    """
    args = [results1]
    mycursor.execute(sql,args)
    answer = mycursor.fetchall()

    return render_template("stadium.html", data = data, answer = answer)

@app.route("/maxPeople", methods = ['POST', "GET"])
def maxPeople():
    c = sqlite3.connect(r"boxing.sqlite")
    mycursor = c.cursor()
    mycursor.execute("SELECT * FROM Stadium")
    data = mycursor.fetchall()
    results1 = request.form['name']
    sql = """
    SELECT st_name, st_maxpeople
    FROM Stadium
    WHERE st_maxpeople >= ?
    """
    args = [results1]
    mycursor.execute(sql,args)
    answer = mycursor.fetchall()
    

    return render_template("stadium.html", data = data, info = answer)


#ROUTING FOR INFO PAGE
@app.route("/info")
def info():
    return render_template("info.html")





    # gonna show the user how much money a selected fighter has made 
@app.route("/MoneySponsor",methods = ['POST', "GET"])
def MoneySponsor():
    results1 = request.form['fighter1']
    print(results1)
    database = r"boxing.sqlite"
    conn = openConnection(database)
    _conn = conn.cursor()
    sql = """ select sum(s_pay)
    FROM Fighters, Sponsors, SponsoredFighter
    where f_name = ?
    and s_sponsorKey = sp_sponsorKey
    and f_fighterKey = sp_fighterKey
    """
    args = [results1]
    _conn.execute(sql,args)
    query = _conn.fetchall()
    print(query)
    _conn.execute("SELECT s_name FROM Sponsors")
    data = _conn.fetchall()


    return render_template("sponsor.html",fighter = query, data = data, name = results1)


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