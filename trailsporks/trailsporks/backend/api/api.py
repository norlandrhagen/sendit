from flask import Flask
from flask_restful import Resource, Api
from db import db

from resources.trail_res import Trail
from resources.trail_trajectory_res import TrailTrajectory
from resources.trail_rating_res import TrailRating

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Trail, "/trail/<string:name>")
api.add_resource(TrailTrajectory, "/trailtrajectory/<int:id>")
api.add_resource(TrailRating, "/trailrating/<string:rating>")
if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
