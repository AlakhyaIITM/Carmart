from datetime import datetime
import json
from extensions import db 

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)

    kilometers_driven = db.Column(db.String(20))
    fuel_type = db.Column(db.String(20))
    transmission = db.Column(db.String(20))
    color = db.Column(db.String(20))
    owner_number = db.Column(db.String(10))
    manufacturing_year = db.Column(db.String(10))
    registration_year = db.Column(db.String(10))
    registration_type = db.Column(db.String(50))
    location = db.Column(db.String(100))

    seller_name = db.Column(db.String(100))
    seller_contact = db.Column(db.String(100))

    specifications = db.Column(db.Text)  # Stored as JSON
    features = db.Column(db.Text)        # Stored as JSON list

    image_filenames = db.Column(db.Text)  # Stored as JSON list
    last_updated = db.Column(db.String(50), default=lambda: datetime.now().strftime('%d %b %Y, %I:%M %p'))

    def get_specifications(self):
        return json.loads(self.specifications or "{}")

    def get_features(self):
        return json.loads(self.features or "[]")

    def get_images(self):
        return json.loads(self.image_filenames or "[]")

    def set_specifications(self, spec_dict):
        self.specifications = json.dumps(spec_dict)

    def set_features(self, features_list):
        self.features = json.dumps(features_list)

    def set_images(self, image_list):
        self.image_filenames = json.dumps(image_list)
