from flask import Flask, jsonify, request
import mongoengine as db
import json

# Create Flask application object
app = Flask(__name__)

# Create connection to CKCS145 MongoDB database
client = db.connect('CKS145', username='', password='')

# Data Class for accessing MongoDB collection
class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True)
    meta = {'collection': 'User', 'allow_inheritance': False}

# A test route to determine if Flask application is initialized properly.
# http://localhost:5000/test
@app.route('/test', methods=['GET'])
def test_route():
    return 'test'

# A route to list all users.
# http://localhost:5000/user/list
@app.route('/user/list', methods=['GET'])
def list_all_users():
    users = User.objects()
    return jsonify(json.loads(users.to_json()))

# A route that allows the insertion of a single user.
# http://localhost:5000/user/insert
@app.route('/user/insert', methods=['POST'])
def create_user():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    
    # Create a user object with above data
    new_user = User(name=name, email=email)
    
    # Persist user object to database
    new_user.save()
    
    # Return the newly created user object in JSON format
    return jsonify(json.loads(new_user.to_json()))

# A route that allows searching for a single user in the database.
# http://localhost:5000/user/find
@app.route('/user/find', methods=['POST'])
def find_a_user():
    # Retrieve data from the HTML form
    name = request.form.get('user_name')
    
    # Find all users that match the name
    users = User.objects(name=name)
    
    # Get the first user that matches
    user = users.first()
    
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(json.loads(user.to_json()))

# A route that allows the deletion of a single user.
# http://localhost:5000/user/delete
@app.route('/user/delete', methods=['POST'])
def delete_user():
    # Retrieve data from the HTML form
    name = request.form.get('user_name')
    
    # Find all users that match the name
    users = User.objects(name=name)
    
    # Get the first user that matches
    user = users.first()
    
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
        status_message = f"{user.name} has been deleted"
        return jsonify({'status': status_message})

if __name__ == '__main__':
    app.run(debug=True)
