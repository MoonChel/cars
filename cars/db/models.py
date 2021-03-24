from gino import Gino

db = Gino()


class Car(db.Model):
    __tablename__ = "car"

    id = db.Column(db.Integer, primary_key=True)
    car_type = db.Column(db.String)
    year = db.Column(db.Integer)
    name = db.Column(db.String)
