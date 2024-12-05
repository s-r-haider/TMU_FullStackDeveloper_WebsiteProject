from flask import Flask, request, jsonify 
from dataclasses import dataclass 
from flask_sqlalchemy import SQLAlchemy   


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:torontomet123@localhost/CKCS145' 
db = SQLAlchemy(app)   

@dataclass 
class User(db.Model):
     __tablename__ = 'User'   
     email: str      
     name: str
      
                
     email = db.Column( db.String(), primary_key=True )
     name = db.Column( db.String(100) )
         
@app.route('/list') 

def list_all():
     all_users = User.query.all()
     print( all_users )      
     return all_users    

@app.route('/insert', methods=['POST']) 
def insert_user():
     name = request.form.get('user_name')
     email = request.form.get('user_email')
     u1 = User(email=email, name=name)
     db.session.add(u1)
     db.session.commit()      
     db.session.flush()          
     status_message = 'row with primary key of ' + email + ' has been inserted'         
     return jsonify( {'status': status_message } )   
# should always be at the end of your file 
if __name__ == '__main__':
    app.run()
