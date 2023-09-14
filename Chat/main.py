from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "titkoskulcs"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

"""Felhasználók tábla létrehozása az adatbázisban"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


"""Az első oldal, ahol a felhasználók bejelentkezhetnek vagy regisztrálhatnak"""


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        """Ellenőrizd a felhasználónevet és a jelszót az adatbázisban"""
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            """ Bejelentkezés sikerült, mentjük a session-be a felhasználónevet"""
            session["username"] = username
            flash("Sikeres bejelntkezés!", "success")
            return redirect(url_for("dashboard"))
        else:
            flas("Hibás felhasználónév vagy jelszó!", "danger")

    return render_template("login.html")


"""Regisztrációs oldal"""


@app.route("/register", methods=["Get", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        """Ellenőrizd, hogy a felhasználónév létezik-e az adatbázisban"""
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("A felhasználónév már foglalt!", "danger")
        else:
            """Ha nincs ilyen felhasználónév, hozz létre egy új felhasználót"""
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Sikeres regisztráció!", "success")
            return redirect(url_for("login"))

    return render_template("register.html")


"""Kijelentkezés"""


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Sikeres kijelentkezés!", "success")
    return redirect(url_for("login"))


"""Fő oldal, ahol bejelentkezett felhasználók találhatók"""


def dashboard():
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])
    else:
        flash("Nincs bejelntkezett felhasználó", "warning")
        return redirect(url_for("login"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
