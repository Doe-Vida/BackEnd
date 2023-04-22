from . import db
import json

# defines model for user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    birthdate = db.Column(db.String(10))
    blood_type = db.Column(db.String(3))
    phone = db.Column(db.String(11))
    sex = db.Column(db.Boolean)
    qty_donations = db.Column(db.Integer)
    date_last_donation = db.Column(db.String(10))
    state = db.Column(db.String(30))
    city = db.Column(db.String(60))

    def __repr__(self):
        return '<User %r>' % self.username
    
    def to_dict(self):
            return {
                'id': str(self.id),
                'username': self.username,
                'password': self.password,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'birthdate': self.birthdate,
                'blood_type': self.blood_type,
                'phone': self.phone,
                'sex': bool(self.sex),
                'qty_donations': (self.qty_donations),
                'date_last_donation': self.date_last_donation,
                'state': self.state,
                'city': self.city
            }

    
