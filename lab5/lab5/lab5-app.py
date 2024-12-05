from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy#from sqlalchemy import Column, Integer, String, ForeignKey

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:torontomet123@localhost/CKCS145'

db = SQLAlchemy(app)
# A test route to determine if Flask application is initialized properly.
# http://localhost:5000/test

@app.route('/test', methods=['GET'])
def test_route() :
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)