from datetime import datetime
import json
from extensions import db

class Cab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    seating_capacity = db.Column(db.Integer, nullable=False)
    ac = db.Column(db.Boolean, default=False)

    # Relationship with CabImage model
    images = db.relationship('CabImage', backref='cab', lazy=True)

    def __repr__(self):
        return f"<Cab {self.make} {self.model}>"

    def get_images(self):
        return [img.filename for img in self.images]

class CabImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    cab_id = db.Column(db.Integer, db.ForeignKey('cab.id'), nullable=False)

    def __repr__(self):
        return f"<CabImage {self.filename}>"
