from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "hey flask"

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
# db = SQLAlchemy(app)
# ma = Marshmallow(app)

# class Car(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     year = db.Column(db.String(4), unique=False)
#     make = db.Column(db.String(50), unique=False)
#     model = db.Column(db.String(50), unique=False)
#     condition = db.Column(db.String(50), unique=False)

#     def __init__(self, year, make, model, condition):
#         self.year = year
#         self.make = make
#         self.model = model
#         self.condition = condition


        

# class CarSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'year', 'make', 'model', 'condition')


# car_schema = CarSchema()
# multiple_car_schema = CarSchema(many=True)
# # guides_schema = GuideSchema(many=True)

# # Endpoint to create a new guide
# @app.route('/car/add', methods=["POST"])
# def add_car():
#     if request.content_type != 'application/json':
#         return jsonify("Error: data must be json.")

#     post_data = request.get_json()
#     year = post_data.get("year")
#     make = post_data.get("make")
#     model = post_data.get("model")
#     condition = post_data.get("condition")

#     new_car = Car(year, make, model, condition)

#     db.session.add(new_car)
#     db.session.commit()

#     car = car.query.get(new_car.id)

#     return car_schema.jsonify(car)


# # Endpoint to query all guides
# @app.route("/cars/get", methods=["GET"])
# def get_cars():
#     all_cars = Car.query.all()
#     result = cars_schema.dump(all_cars)
#     return jsonify(result)

# #endpoint fro querying a single guide
# @app.route("/car/get/<id>", methods=["GET"])
# def get_car(id):
#     car = Car.query.get(id)
#     return car_schema.jsonify(car)

# # Endpoint for updating a guide
# @app.route("/car/put/<id>", methods=["PUT"])
# def car_update(id):
#     car = Car.query.get(id) 
#     year = request.json['year']
#     make = request.json['make']
#     model = request.json['model']
#     condition = request.json['condition']

#     car.year = year
#     car.make = make
#     car.model = model
#     car.condition = condition


#     db.session.commit()
#     return car_schema.jsonify(car)


# #endpoint for deleting a record
# @app.route("/car/delete/<id>", methods=["DELETE"])
# def car_delete(id):
#     car = Car.query.get(id)
#     db.session.delete(car)
#     db.session.commit()
    
#     return "car was deleted"


if __name__ == '__main__':
    app.run(debug=True)