from .db import db

class Messages(db.Model):
    __tablename__ = "Messages"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userid_sent = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    userid_received = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=False)
    
    