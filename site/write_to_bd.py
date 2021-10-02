import datetime

from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    articul = db.Column(db.String)
    name = db.Column(db.String)
    price_new = db.Column(db.String)
    price_old = db.Column(db.String)
    brend = db.Column(db.String)
    link = db.Column(db.String)
    all_prices = db.Column(db.String)

    def __repr__(self):
        return '<Products %r' % self.id


def write(category, articul, name, price_new, price_old, brend, link):
    x_date = str(datetime.datetime.now().strftime("%d.%m.%Y"))
    a = db.session.query(Products).filter(Products.link == link).first()
    if a is None:
        transactions = Products(category=category, articul=articul, name=name, price_new=price_new, price_old=price_old,
                                brend=brend, link=link, all_prices=str([[price_new, x_date]]))
        try:
            db.session.add(transactions)
            db.session.commit()
            return 'Ok'
        except:
            return "Error"
    else:
        a.category, a.articul, a.name, a.price_new, a.price_old, a.brend = category, articul, name, price_new, price_old, brend
        x = eval(a.all_prices)
        x.append([price_new, x_date])
        a.all_prices = str(x)
        try:
            db.session.commit()
            return 'Ok'
        except:
            return 'Error'
