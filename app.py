from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name = "Севастьян", user = 101)

@app.route("/Main/")
def main():
    return "Main"

@app.route("/Catalog/")
def catalog():
    return "Catalog"

@app.route("/AboutUs/")
def AboutUs():
    return "AboutUs"

@app.route("/AboutCompany/")
def AboutCompany():
    return "AboutCompany"

@app.route("/Profile/")
def profile():
    return "Profile"


if __name__ == "__main__":
    app.run()