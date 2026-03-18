from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    dob = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    parent_name = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(120))
    address = db.Column(db.Text)
    grade = db.Column(db.String(20))

    def __repr__(self):
        return f"<Student {self.first_name}>"
