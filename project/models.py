from project import app
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy(app)

class user(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    pnom=db.Column(db.String(50))
    email=db.Column(db.String(100), unique=True)
    password=db.Column(db.String(50))
db.create_all()  


