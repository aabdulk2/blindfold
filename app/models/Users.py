from flask_login import UserMixin
from .db import db

class Users(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    preference = db.Column(db.String(10), nullable=False)
    bio = db.Column(db.String(600), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(600), nullable=False)
    
    messages = db.relationship("Messages", backref="Users")

    def to_json(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'gender': self.gender,
            'bio': self.bio,
            'email': self.email,
            'preference': self.preference,
            'username': self.username,
            'age': self.age
        }
    