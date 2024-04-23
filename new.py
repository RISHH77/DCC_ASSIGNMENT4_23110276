from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Stargate@123'
app.config['MYSQL_DB'] = 'dcc_assignment'

mysql = MySQL(app)

# @app.route('/', methods = ["POST", "GET"])
# def main_page():
#     return render_template("index.html")

@app.route('/', methods=["POST", "GET"])
def a_1():
    if request.method == "GET":
        print(request.method)
        cursor = mysql.connection.cursor()
        cursor.execute("SHOW COLUMNS FROM encashed")  
        columns = [column[0] for column in cursor.fetchall()] 
        cursor.execute("SELECT distinct `NameofthePurchaser` FROM dcc_assignment.purchased") 
        companies = [i[0] for i in cursor.fetchall()]
        cursor.execute("SELECT distinct `NameofthePoliticalParty` FROM dcc_assignment.encashed")
        parties = [i[0] for i in cursor.fetchall()] 
        cursor.close()
        return render_template("index.html", columns=columns, companies=companies, parties = parties)
    return render_template("index.html")


@app.route('/', methods=["POST", "GET"])
def q2_1():
    if request.method == "GET":
        print('HI')
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT distinct `Name of the Purchaser` FROM dcc_assignment.purchased") 
        print(cursor.fetchall()[0][0])
        companies = [i[0] for i in cursor.fetchall()]
        print(companies)
        cursor.close()
        return render_template("index.html", companies=companies)
    print('Bye')
    return render_template("index.html")

@app.route('/', methods=["POST", "GET"])
def q3_1():
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT distinct `NameofthePoliticalParty` FROM dcc_assignment.encashed") 
        print(cursor.fetchall()[0][0])
        companies = [i[0] for i in cursor.fetchall()]
        print(companies)
        cursor.close()
        return render_template("index.html", companies=companies)
    return render_template("index.html")

@app.route('/', methods=["POST", "GET"])
def q4_1():
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT distinct `NameofthePoliticalParty` FROM dcc_assignment.encashed") 
        print(cursor.fetchall()[0][0])
        companies = [i[0] for i in cursor.fetchall()]
        print(companies)
        cursor.close()
        return render_template("index.html", companies=companies)
    return render_template("index.html")

@app.route('/', methods=["POST", "GET"])
def q5_1():
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT distinct `NameofthePurchaser` FROM dcc_assignment.purchased") 
        print(cursor.fetchall()[0][0])
        companies = [i[0] for i in cursor.fetchall()]
        print(companies)
        cursor.close()
        return render_template("index.html", companies=companies)
    return render_template("index.html")

@app.route('/', methods=["POST", "GET"])
def q6_1():
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT distinct `NameofthePoliticalParty` FROM dcc_assignment.encashed") 
        print(cursor.fetchall()[0][0])
        companies = [i[0] for i in cursor.fetchall()]
        print(companies)
        cursor.close()
        return render_template("index.html", companies=companies)
    return render_template("index.html")

@app.route('/a_1', methods = ["POST", "GET"])
def a_2():
    if request.method == "POST":
        print(request.method)
        print(request.form["value"])  
        print("TEST")
        value = request.form["value"]
        column = request.form["selected_column"]
        cursor = mysql.connection.cursor()
        print(request.form["selected_column"])
        cursor.execute(f'select * from encashed where `{column}` like "{value}"')
        data = cursor.fetchall()
        print(data)        
        cursor.close()
    return render_template("first.html", data_a1 = data, column = column, value = value) 
 

@app.route("/q21",methods=["GET","POST"])
def q_2():
    if request.method=="POST":
        comp=request.form["buyer"]
        cursor = mysql.connection.cursor()
        cursor.execute(f'select Denominations from purchased where NameofthePurchaser = "{comp}"')
        b=cursor.fetchall()
        cursor.execute(f'select DateofPurchase from purchased where NameofthePurchaser = "{comp}"')
        c=cursor.fetchall()
        cursor.execute(f'select count(Denominations) from purchased where NameofthePurchaser = "{comp}"')
        count = cursor.fetchall()
        empty = [0 for i in range(len(b))]
        if (len(b)!=0 and len(c)!=0):
            y19, y20, y21, y22, y23, y24=0,0,0,0,0,0
            for i in range(len(b)):
                empty[i] = int(''.join(b[i]).replace(",", ""))
            for i in range(len(c)):
                if c[i][0][-2:]=='19':
                     y19+=int(empty[i])
                elif c[i][0][-2:]=='20':
                     y20+=int(empty[i])
                elif c[i][0][-2:]=='21':
                     y21+=int(empty[i])
                elif c[i][0][-2:]=='22':
                     y22+=int(empty[i])
                elif c[i][0][-2:]=='23':
                     y23+=int(empty[i])
                elif c[i][0][-2:]=='24':
                     y24+=int(empty[i])
            d=[y19,y20,y21,y22,y23,y24]
            e=['19','20','21','22','23','24']
            data = {'labels' : e, 'values':d}
            print(d)
            return render_template("first.html",money=d,year=e, count = count, data = data)
        
@app.route("/q31",methods=["GET","POST"])
def q_3():
    if request.method=="POST":
        comp=request.form["party"]
        cursor = mysql.connection.cursor()
        cursor.execute(f'select Denominations from encashed where NameofthePoliticalParty = "{comp}"')
        b=cursor.fetchall()
        cursor.execute(f'select DateofEncashment from encashed where NameofthePoliticalParty = "{comp}"')
        c=cursor.fetchall()
        cursor.execute(f'select count(Denominations) from encashed where NameofthePoliticalParty = "{comp}"')
        count = cursor.fetchall()
        empty = [0 for i in range(len(b))]
        if (len(b)!=0 and len(c)!=0):
            y19, y20, y21, y22, y23, y24=0,0,0,0,0,0
            for i in range(len(b)):
                empty[i] = int(''.join(b[i]).replace(",", ""))
            for i in range(len(c)):
                if c[i][0][-2:]=='19':
                     y19+=int(empty[i])
                elif c[i][0][-2:]=='20':
                     y20+=int(empty[i])
                elif c[i][0][-2:]=='21':
                     y21+=int(empty[i])
                elif c[i][0][-2:]=='22':
                     y22+=int(empty[i])
                elif c[i][0][-2:]=='23':
                     y23+=int(empty[i])
                elif c[i][0][-2:]=='24':
                     y24+=int(empty[i])
            d=[y19,y20,y21,y22,y23,y24]
            e=['19','20','21','22','23','24']
            data = {'labels' : e, 'values':d}
            print(d)
            return render_template("first.html", encashed=d,year=e, count = count, data = data)
        
@app.route("/q41",methods=["GET","POST"])
def q_4():
    if request.method=="POST":
        cursor = mysql.connection.cursor()
        par=request.form["party"]
        cursor.execute("Select purchased.Denominations, NameofthePurchaser from  purchased inner join encashed where encashed.BondNumber = purchased.bond and purchased.Prefix = encashed.Prefix and encashed.NameofthePoliticalParty= %s",(par,))
        merged=cursor.fetchall()
        dictt={}
        if len(merged)==0:
            return render_template("notavailable.html")
        else:
            for i in merged:
                if i[1] not in dictt:
                   dictt[i[1]]=0
                dictt[i[1]]+=int(i[0].replace(",",""))
        companies = []
        total = 0
        for i in dictt:
            companies.append([i,dictt[i]])
            total += dictt[i]
        return render_template("first.html",person=companies,total=total)

@app.route("/q51",methods=["GET","POST"])
def q_5():
        cursor = mysql.connection.cursor()
        if request.method=="POST":
            cursor.execute("Select encashed.Denominations,NameofthePoliticalParty from  encashed inner join purchased where encashed.BondNumber = purchased.bond and purchased.Prefix = encashed.Prefix and purchased.NameofthePurchaser=%s",(request.form["buyer"],))
            fetched_values=cursor.fetchall()
            l={}

            for i in fetched_values:
                if i[1] not in l:
                    l[i[1]]=0
                l[i[1]]+=int(i[0].replace(",",""))
            k=[]
        s=0
        for i in l:
            k.append([i,l[i]])
            s+=l[i]
        return render_template("first.html",party=k,total=s)
@app.route("/q61",methods=["GET","POST"])
def q_6():
    cursor = mysql.connection.cursor()
    if request.method=="POST":
        list1=[]
        list2=[]
        cursor.execute("select distinct NameofthePoliticalParty from encashed")
        l=list(cursor.fetchall())

        for i in l:
            cursor.execute("Select Denominations from encashed where NameofthePoliticalParty=%s",(i[0],))
            fetched_values=cursor.fetchall()
            s=0
            for j in fetched_values:
                s+=int(j[0].replace(",",""))
            list1.append([i[0]])
            list2.append(s)
        return render_template("first.html",party_values=list2,labels=list1)
    
if __name__ == '__main__':

   app.run(host="0.0.0.0", port="80", debug = True)