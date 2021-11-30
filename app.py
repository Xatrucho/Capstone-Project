from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "hey flask"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

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
@app.route('/add-estimate', methods=["POST"])
def add_estimate():
    post_data = request.get_json()
    year = request.json['year']
    make = request.json['make']
    model = request.json['model']
    condition = request.json['condition']

    new_estimate = Estimate(year, make, model, condition)

    db.session.add(new_estimate)
    db.session.commit()

    estimate = Estimate.query.get(new_estimate.id)

    return estimate_schema.jsonify(estimate)

# Endpoint to query all estimates
@app.route("/estimates", methods=["GET"])
def get_estimates():
    all_estimates = Estimate.query.all()
    result = estimates_schema.dump(all_estimates)
    return jsonify(result)


# # Endpoint to query all estimates-(different version)
# @app.route("/estimates", methods=["GET"])
# def get_estimates():
#     all_estimates = db.session.query(Estimate).all()
#     return jsonify(estimates_schema.dump(all_estimates))


#endpoint fro querying a single guide
@app.route("/estimate/<id>", methods=["GET"])
def get_estimate(id):
    estimate = Estimate.query.get(id)
    return estimate_schema.jsonify(estimate)



# # Endpoint for updating a estimate
@app.route("/estimate/<id>", methods=["PUT"])
def estimate_update(id):
    estimate = Estimate.query.get(id) 
    year = request.json['year']
    make = request.json['make']
    model = request.json['model']
    condition = request.json['condition']

    estimate.year = year
    estimate.make = make
    estimate.model = model
    estimate.condition = condition


    db.session.commit()
    return estimate_schema.jsonify(estimate)


# #endpoint for deleting a record
@app.route("/estimate/<id>", methods=["DELETE"])
def estimate_delete(id):
    estimate = Estimate.query.get(id)
    db.session.delete(estimate)
    db.session.commit()
    
    # return estimate_schema.jsonify(estimate)
    return "Estimate was deleted"


if __name__ == '__main__':
    app.run(debug=True)