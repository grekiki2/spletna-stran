from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/test/<username>')
def test(username):
    return render_template("test.html", username=username)

@app.route('/form_test/')
def form_test():
    return render_template("form_test.html")

@app.route('/form-submit/')
def form_submit():
    uporabnisko_ime = request.args.get("username")
    geslo = request.args.get("geslo")
    print(uporabnisko_ime, geslo)
    if uporabnisko_ime == "admin" and geslo == "1234":
        return "Hvala za oddajo"
    else:
        return render_template("form_test.html", info_text = "Prijava ni uspela")

@app.route('/view_db/')
def view_db():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("select * from contacts;")
    return cursor.fetchall()


@app.route('/registracija/')
def registracija():
    return render_template("registracija.html")

@app.route('/registracija-submit/')
def registracija_submit():  
    uporabnisko_ime = request.args.get("username")
    geslo = request.args.get("geslo")

    insert_command = 'INSERT INTO contacts(first_name, last_name) VALUES("'+uporabnisko_ime+'", "'+geslo+'");'
    print(insert_command)
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(insert_command)
    conn.commit()
    return "V izdelavi"

app.run(debug=True)

