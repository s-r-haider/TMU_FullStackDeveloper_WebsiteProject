from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

@app.route('/home', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        data = 'hello world'
        return jsonify({'data': data})
    

@app.route('/home/<int:num>', methods = ['GET'])

def disp(num):
    return jsonify({'data': num**2})

 
app.run( debug=True )
