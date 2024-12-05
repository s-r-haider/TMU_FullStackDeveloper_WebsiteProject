# always at the top of fle

import random

from flask import Flask, request, jsonify

from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:torontomet123@localhost/CKCS145'
db = SQLAlchemy(app)

@dataclass
class Student(db.Model):
    __tablename__ = 'Students'
    
    email: str
    firstName: str
    lastName: str
    studentNo: int
    
    email = db.Column( db.String(100) )
    firstName = db.Column( db.String(100) )
    lastName = db.Column( db.String(100) )
    studentNo = db.Column( db.Integer(), primary_key=True )

# http://localhost:5000/list
@app.route('/list')
def list_all() :
    all_students = Student.query.all()
    print( all_students )
    
    return all_students  

# http://localhost:5000/insert
@app.route('/insert', methods=['POST'])
def insert_student():
    
    first_name_val = request.form.get('first_name')
    last_name_val = request.form.get('last_name')
    email_val = request.form.get('student_email')
    
    student_no_val = random.randint(1, 1000000)
    
    
    print( first_name_val, last_name_val, email_val, student_no_val)
    
    new_student = Student(email=email_val, firstName=first_name_val, lastName=last_name_val, studentNo=student_no_val )
    db.session.add(new_student)
    db.session.commit()
    db.session.flush()
    
    status_message = 'working'
    
    return jsonify( {'status': status_message } )

# http://localhost:5000/update
@app.route('/update', methods=['POST'])
def update_student():
    
    first_name_val = request.form.get('first_name')
    last_name_val = request.form.get('last_name')
    email_val = request.form.get('student_email')
    student_no_val = request.form.get('student_no')
    
    query = db.session.query(Student)
    query = query.filter(Student.studentNo==student_no_val)
    rows_changed = query.update({Student.firstName: first_name_val, Student.lastName: last_name_val })
    
    print ('rows_changed : ', rows_changed)
    print('query :', query)
    
    db.session.commit()
    db.session.flush()
    
    status_message = str(rows_changed) + ' rows have been affected/changed'
    
    return jsonify( {'status': status_message } )

# http://localhost:5000/delete
@app.route('/delete', methods=['POST'])
def delete_student():
    
    student_no_val = request.form.get('student_no')
    
    query = db.session.query(Student)
    query = query.filter(Student.studentNo==student_no_val)
    
    rows_changed = query.delete( ) 
   
    print ('rows_changed : ', rows_changed)
    print('query :', query)
    
    db.session.commit()
    db.session.flush()
    
    status_message = str(rows_changed) + ' rows have been affected/changed'
    
    return jsonify( {'status': status_message } )


# should always be at the end of your file
if __name__ == '__main__' :
  app.run( debug=True )
