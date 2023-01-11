from .db import db

class Reports(db.Model):
    __tablename__ = "Reports"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userid_reported = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    userid_reporting = db.Column(db.Integer, nullable=False)
    report = db.Column(db.Text, nullable=False)