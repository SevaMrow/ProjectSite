from flask import Flask,render_template
from models import get_db_connection

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Main/")
def main():
    return render_template("meny.html")

@app.route("/Catalog/")
def catalog():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template("catalog.html", products=products)

@app.route("/AboutUs/")
def AboutUs():
    return render_template("aboutus.html")

@app.route("/AboutCompany/")
def AboutCompany():
    return render_template("company.html")

@app.route("/Profile/")
def profile():
    return render_template("profile.html")

@app.route("/Order/<id>")
def order(id):
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products where id = ' + id).fetchall()
    conn.close()
    return render_template("order.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)