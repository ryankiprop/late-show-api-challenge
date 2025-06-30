from ..models import db
from datetime import date

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today())
    number = db.Column(db.Integer, nullable=False, unique=True)

    appearances = db.relationship('Appearance', backref='episode', lazy=True, cascade='all, delete-orphan')