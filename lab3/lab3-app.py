from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

@app.route('/home', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        data = 'hello world'
        return jsonify({'data': data})
    if(request.method == 'POST'):
        data = request.get_json()
        return jsonify(data)

@app.route('/home/<int:num>', methods = ['GET'])

def disp(num):
    return jsonify({'data': num**2})

@app.route('/test', methods = ['POST'])

def post_test_route():
    if(request.method == 'POST'):
        data_id = request.json.get('Id')
        data_customer = request.json.get('Customer')
        data_quantity = request.json.get('Quantity')
        data_price = request.json.get('Price')
        print('Id: ', data_id)
        print('Customer', data_customer)
        print('Quantity', data_quantity)
        print('Price', data_price)
    return jsonify({'data': 'success'})
 
app.run( debug=True )
