from flask import Flask, jsonify, request
app = Flask(__name__)

# Route for addition
@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'Error': 'Please provide two numbers'}), 400
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2
        return jsonify({'Result': result}), 200
    except ValueError:
        return jsonify({'Error': 'Invalid numbers provided'}), 400

# Route for holiday information
@app.route('/holiday/<name>', methods=['GET'])
def get_holiday_details(name):
    holiday_details = {
        "christmas": "Christmas is celebrated on December 25th.",
        "thanksgiving": "Thanksgiving is celebrated on the fourth Thursday of November.",
        "newyears": "New Year's Day is celebrated on January 1st",
        "mlk": "Martin Luther King Jr. Day is celebrated on the third Monday of January",
        "july4": "Independece Day is celebrated on July 4th",
        "veterans": "Veteran's Day is celebrated on November 11th"
    }
    if name.lower() in holiday_details:
        return jsonify({'Information': holiday_details[name.lower()]}), 200
    else:
        return jsonify({'Error': 'Holiday information not available'}), 404

# Route for handling unknown instructions
@app.errorhandler(404)
def unknown_instruction(error):
    return jsonify({'Error': 'Unknown instructions'}), 404

if __name__ == '__main__':
    app.run(debug=True)


# curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://localhost:5000/add
# curl http://localhost:5000/holiday/<HOLIDAYNAME>
