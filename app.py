from flask import Flask, jsonify, request
from get_results import getNutritionInfo

app = Flask(__name__)




@app.route('/getInfo', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        data = request.data
        print('here')
        
        result = getNutritionInfo(data)
        
        return jsonify({'response': 'Data received', 'Result': result}), 200
    else:
        print('here')
        # For GET requests, just send back a simple message
        return jsonify({'message': 'This is a GET request'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
