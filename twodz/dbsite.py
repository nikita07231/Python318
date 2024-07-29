from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from FDataBase import FDataBase


DEBUG = True
SECRET_KEY = '13e72478198a5cd2af3a76874dff95c79b3e31e6'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flask11.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', "r") as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', curs=dbase.get_posts_annonce())


@app.route("/add_curs", methods=["POST", "GET"])
def add_curs():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["curs"]) > 10:
            res = dbase.add_curs(request.form["name"], request.form["price"], request.form["curs"])
            if not res:
                flash("Ошибка добавления курса", category='error')
            else:
                flash("Курс добавлен успешно", category="success")
        else:
            flash("Ошибка добавления курса", category='error')

    return render_template('add_curs.html', title="Добавление курса")


@app.route("/info")
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run()
