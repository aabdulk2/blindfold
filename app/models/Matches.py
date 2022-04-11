from .db import db

class Matches(db.Model):
    userid_Matched = db.Column(db.Integer, primary_key=True, nullable=False)
    userid_Matching = db.Column(db.Integer, primary_key=True, nullable=False)
    