from extensions import db

class Bus(db.Model):
    __tablename__ = 'buses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    seating_capacity = db.Column(db.Integer, nullable=False)
    image_filename = db.Column(db.String(200))

    def get_image(self):
        return self.image_filename if self.image_filename else 'default-bus.jpg'
