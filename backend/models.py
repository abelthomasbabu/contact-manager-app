from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(90), unique=False, nullable=False)
    last_name = db.Column(db.String(90), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    #take all of the fields of our object and convert into a python dictionary to json and pass from our api [json - javascript object notation]
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }