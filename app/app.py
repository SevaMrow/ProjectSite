from flask import Flask,render_template,request,redirect
from models import get_db_connection

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('http://127.0.0.1:5000/Main/')

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

@app.route("/Order/<id>", methods=['post', 'get'])
def order(id):
    if request.method == "POST":
        user = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        print(user)
        conn = get_db_connection()
        sql  = f'INSERT INTO orders (name_user,email,number,text) VALUES ("{user}","{email}","{number}","{id}")'
        print(sql)
        conn.execute(sql)
        conn.commit()
        print("Отправка данных прошла")
        conn.close()

    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products where id = ' + id).fetchall()
    conn.close()
    return render_template("order.html", products=products)

@app.route("/admin/")
def admin():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM orders').fetchall()
    return render_template("admin.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)