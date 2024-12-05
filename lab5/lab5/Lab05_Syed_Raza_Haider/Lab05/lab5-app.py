from flask import Flask, request, jsonify 
from dataclasses import dataclass 
from flask_sqlalchemy import SQLAlchemy   


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:raza@localhost/CKCS145' 
db = SQLAlchemy(app)   

@dataclass 
class User(db.Model):
     __tablename__ = 'User'   
     email: str      
     name: str               
     email = db.Column( db.String(), primary_key=True )
     name = db.Column( db.String() )

@app.route('/test', methods=['GET'])
def test_route() :
    return 'test'

@app.route('/list') 
def list_all():
     all_users = User.query.all()
     print( all_users )      
     return all_users    

@app.route('/user/list', methods=['GET'])
def list_all_users():
    result_set = db.session.query( User ).all()
    return jsonify( result_set )

# A route that allows the insertion for a single user.
# http://localhost:5000/user/insert
@app.route('/user/insert', methods=['POST'])
def insert_user():
    name_val = request.form.get('user_name')
    email_val = request.form.get('user_email')
    print( 'data submitted:', name_val, email_val )
    new_user = User(email=email_val, name=name_val )
    db.session.add(new_user)
    db.session.commit()
    db.session.flush()
    status_message = 'working'       
    return jsonify( {'status': status_message } )

# A route that allows for changing the name of a single user.
# http://localhost:5000/user/update
@app.route('/user/update', methods=['POST'])
def update_student():
    name_val = request.form.get('user_name')
    email_val = request.form.get('user_email')
    query = db.session.query(User)
    query = query.filter(User.email==email_val)
    rows_changed = query.update({User.name: name_val, User.name:name_val })
    print ('rows_changed : ', rows_changed)
    print('query :', query)
    db.session.commit()
    db.session.flush()
    status_message = str(rows_changed) + ' rows have been affected/changed'
    return jsonify( {'status': status_message } )

# A route that allows for deleting user.
# http://localhost:5000/user/delete
@app.route('/user/delete', methods=['POST'])
def delete_student():
    email_val = request.form.get('user_email')
    query = db.session.query(User)
    query = query.filter(User.email==email_val)
    rows_changed = query.delete( )
    print ('rows_changed : ', rows_changed)
    print('query :', query)
    db.session.commit()
    db.session.flush()
    status_message = str(rows_changed) + ' rows have been affected/changed'
    return jsonify( {'status': status_message } )

# should always be at the end of your file 
if __name__ == '__main__':
    app.run()
