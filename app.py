from flask import Flask, render_template, request, redirect, jsonify
from models import db, Student

app = Flask(__name__)

# DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create DB
with app.app_context():
    db.create_all()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form

    student = Student(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        dob=data.get('dob'),
        gender=data.get('gender'),
        parent_name=data.get('parent_name'),
        phone=data.get('phone'),
        email=data.get('email'),
        address=data.get('address'),
        grade=data.get('grade')
    )

    db.session.add(student)
    db.session.commit()

    return redirect('/success')

@app.route('/success')
def success():
    return "Admission Form Submitted Successfully!"

@app.route('/students')
def students():
    all_students = Student.query.all()
    return jsonify([
        {
            "id": s.id,
            "name": s.first_name + " " + s.last_name,
            "grade": s.grade
        } for s in all_students
    ])

if __name__ == '__main__':
    app.run(debug=True)
