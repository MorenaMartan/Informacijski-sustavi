from app import db


class Usluga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    

    def __init__(self, name, price):
        self.name = name
        self.price = price
       