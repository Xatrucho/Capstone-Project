from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "hey flask"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Estimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(4), unique=False)
    make = db.Column(db.String(50), unique=False)
    model = db.Column(db.String(50), unique=False)
    condition = db.Column(db.String(50), unique=False)

    def __init__(self, year, make, model, condition):
        self.year = year
        self.make = make
        self.model = model
        self.condition = condition


class EstimateSchema(ma.Schema):
    class Meta:
        fields = ('year', 'make', 'model', 'condition')


estimate_schema = EstimateSchema()
estimates_schema = EstimateSchema(many=True)
# guides_schema = GuideSchema(many=True)

# Endpoint to create a new estimate
@app.route('/estimate', methods=["POST"])
def add_estimate():
    year = request.json['year']
    make = request.json['make']
    model = request.json['model']
    condition = request.json['condition']

    new_estimate = Estimate(year, make, model, condition)

    db.session.add(new_estimate)
    db.session.commit()

    estimate = Estimate.query.get(new_estimate.id)

    return estimate_schema.jsonify(estimate)


# # Endpoint to query all estimates
@app.route("/estimates", methods=["GET"])
def get_estimates():
    all_estimates = Estimate.query.all()
    result = estimates_schema.dump(all_estimates)
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True)

#endpoint fro querying a single guide
# @app.route("/car/get/<id>", methods=["GET"])
# def get_car_by_id(id):
#     car = db.session.query(Car).filter(Car.year == year).first()
#     return jsonify(car_schema.(car))

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
#     return jsonify(you got it.)


# #endpoint for deleting a record
# @app.route("/car/delete/<id>", methods=["DELETE"])
# def car_delete(id):
#     car = Car.query.get(id)
#     db.session.delete(car)
#     db.session.commit()
    
#     return "car was deleted"


# if __name__ == '__main__':
#     app.run(debug=True)