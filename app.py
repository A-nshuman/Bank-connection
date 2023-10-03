from flask import Flask, request, render_template, session, g, redirect, url_for, json, flash
from DB_Operations import add_text, check_login_credentials, get_name
import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(host="sql12.freemysqlhosting.net", user="sql12649572", passwd="W7qvB34MYI", database="sql12649572")
cursor = connection.cursor()


app = Flask(__name__, static_folder='static')
app.secret_key = '123456'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        f_name = request.form["f_name"]
        l_name = request.form["l_name"]
        email = request.form["email"]
        uname = request.form["username"]
        upwd = request.form["password"]
        phone = request.form["p_num"]

        san_email = email.replace(".", "_").replace("@", "_")
        formdata = ((f_name, l_name, email, uname, upwd, phone))
        add_new = add_text(formdata, san_email)

        return render_template('login.html')
    else:
        return render_template('register.html')
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        upwd = request.form["upwd"]
        
        if check_login_credentials(email, upwd):
            session['email'] = email
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid email or password. Please try again.")
            return render_template("login.html")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    email = session['email']
    cursor.execute(f"SELECT * from users where email = '{email}'")
    user_data = cursor.fetchall()
    print(user_data)

    if user_data:
            f_name = user_data[0][0].title()
            l_name = user_data[0][1].title()
            balance = user_data[0][-1]
            full_name = f"{f_name} {l_name}"
            print(full_name, f_name, l_name, balance)
            session['bal'] = balance

            return render_template('dashboard.html', full_name=full_name, balance=balance)

    return "User not found"

@app.route("/acc_sum")
def acc_sum():
    cursor = connection.cursor(dictionary=True)

    email = session.get('email', '')
    san_email = email.replace('@', '_').replace('.', '_')
   
    cursor.execute(f"SELECT Statement, entry_datetime FROM {san_email} ORDER BY entry_datetime DESC")
    rows = cursor.fetchall()

    for row in rows:
        row['entry_datetime'] = row['entry_datetime'].strftime("%d/%m/%Y, %I:%M:%S %p")

    return render_template("acc_sum.html", statements=rows)

@app.route("/bal", methods=["GET", "POST"])
def bal():
    email = session.get('email', '')
    san_email = email.replace('@', '_').replace('.', '_')

    if request.method == "POST":    
        amount = float(request.form["amount"])

        cursor.execute(f"update users set balance = balance + {amount} where email = '{email}'")
        cursor.execute(f"insert into {san_email}(Statement) values('₹ {amount} deposited')")
        flash("Amount successfully added to balace")

        connection.commit()

    return render_template('bal.html')

@app.route("/currency")
def currency():
    return render_template('currency.html')

@app.route("/consult")
def consult():
    return render_template('consultant.html')

@app.route("/insurance")
def insurance():
    return render_template('insurance.html')

@app.route("/loan")
def loan():
    return render_template('loan.html')

@app.route("/mut_fund")
def mut_fund():
    return render_template('mut_fund.html')

@app.route("/fixed_dep", methods=["GET", "POST"])
def fixed_dep():
    bal = float(session['bal'])
    if request.method == "POST":
        amount = float(request.form["amount"])
        tenure = int(request.form["tenure"])
        email = session.get('email', '')

        san_email = email.replace('@', '_').replace('.', '_')
        
        if bal > amount:
            cursor.execute(f"insert into {san_email}(Statement) values('FD of ₹ {amount} done at 7.1%')")
            cursor.execute(f"update users set balance = balance - {amount} where email = '{email}'")
            flash("FD done successfully")

            connection.commit()
        else:
            flash("Insufficient balance")

    return render_template('fixed_dep.html')

@app.route("/rec_dep")
def rec_dep():
    bal = float(session['bal'])
    if request.method == "POST":
        amount = float(request.form["amount"])
        tenure = int(request.form["tenure"])
        email = session.get('email', '')

        san_email = email.replace('@', '_').replace('.', '_')
        
        if bal > amount:
            cursor.execute(f"insert into {san_email}(Statement) values('RD of ₹ {amount} done at 7.1%')")
            cursor.execute(f"update users set balance = balance - {amount} where email = '{email}'")
            flash("RD done successfully")

            connection.commit()
        else:
            flash("Insufficient balance")

    return render_template('rec_dep.html')

@app.route("/remit", methods=["GET", "POST"])
def remit():
    bal = float(session['bal'])
    if request.method == "POST":
        amount = float(request.form["amount"])
        rec = request.form["acc"]
        email = session.get('email', '')

        san_email = email.replace('@', '_').replace('.', '_')
        san_rec = rec.replace('@', '_').replace('.', '_')
        
        if bal > amount:
            cursor.execute(f"insert into {san_email}(Statement) values('₹ {amount} sent to {rec}')")
            cursor.execute(f"insert into {san_rec}(Statement) values('₹ {amount} received from {email}')")
            cursor.execute(f"update users set balance = balance - {amount} where email = '{email}'")
            cursor.execute(f"update users set balance = balance + {amount} where email = '{rec}'")
            flash("Amount successfully remitted")

            connection.commit()
        else:
            flash("Insufficient balance")

    return render_template('remit.html')

@app.route("/stocks")
def stocks():
    return render_template('stocks.html')

@app.route("/TandC")
def TandC():
    return render_template('T and C.html')

@app.route("/del_acc", methods=['GET', 'POST'])
def del_acc():
    if request.method == "POST":
        email = session.get('email', '')
        san_email = email.replace('@', '_').replace('.', '_')

        cursor.execute(f"delete from users where email = '{email}'")
        cursor.execute(f"drop table {san_email}")

        return render_template('index.html')
    
    return render_template('del_acc.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
