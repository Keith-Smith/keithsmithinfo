# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(
    username="KeithESmith",
    password="mysqlBlaze",
    hostname="KeithESmith.mysql.pythonanywhere-services.com",
    databasename="KeithESmith$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('test.html', comments=Comment.query.all())
        
    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return render_template('test.html', comments=Comment.query.all())

