from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask.views import MethodView

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class OSVersion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)


class ComputeInstance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    os_version_id = db.Column(
        db.Integer, db.ForeignKey("os_version.id"), nullable=False, default=1
    )
    ip_address = db.Column(db.String(50), nullable=False)
    hostname = db.Column(db.String(50))
    created_at = db.Column(db.Date, default=datetime.utcnow)
    os_version = db.relationship("OSVersion", backref="compute_instances", lazy=True)


# CRUD:

# class ComputeInstanceCRUD(MethodView)
# class OSVersionCRUD(MethodView)
