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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/magazine_id=<string:magazine_id>')
def catalog_page(magazine_id):
    items = Products.query.all()
    if magazine_id == 'perekrestok':
        color = 'secondary'
    else:
        color = 'secondary'
    return render_template('catalog.html', m_name=magazine_id, items=items, color=color)


@app.route('/graph_params=<string:points>')
def item_page(points):
    points = eval(points)
    points1, points2 = [], []
    print(points)
    for i in range(len(points)):
        points1.append(float(points[i][0].replace(',', '.')))
        p = int(points[i][1].split('.')[1])
        points2.append(p)
    points1.append(100)
    print(points2)
    return render_template('graph.html', param=points2, param2=points1)

if __name__ == '__main__':
    app.run(debug=True)
