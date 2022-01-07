from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/cafe")
def get_record():
    cafes = Cafe.query.all()
    output = []
    for cafe in cafes:
        cafe_record = {'cafe_id': cafe.id,
                       'name': cafe.name,
                       'map_url': cafe.map_url,
                       'img_url': cafe.img_url,
                       'location': cafe.location,
                       'seats': cafe.seats,
                       'has_toilet': cafe.has_toilet,
                       'has_wifi': cafe.has_wifi,
                       'has_sockets': cafe.has_sockets,
                       'can_take_calls': cafe.can_take_calls,
                       'coffee_price': cafe.coffee_price
                       }
        output.append(cafe_record)
    return {"cafe": output}


## HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def post_record():
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"),
                    location=request.form.get("loc"),
                    has_sockets=bool(request.form.get("sockets")),
                    has_toilet=bool(request.form.get("toilet")),
                    has_wifi=bool(request.form.get("wifi")),
                    can_take_calls=bool(request.form.get("calls")),
                    seats=request.form.get("seats"),
                    coffee_price=request.form.get("coffee_price"))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify('id', new_cafe.id)


## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
