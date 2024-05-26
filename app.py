from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    name = data['name']
    age = int(data['age'])
    current_year = datetime.now().year
    year_turn_100 = current_year + (100 - age)
    response = {
        "message": f"{name}, you will turn 100 years old in the year {year_turn_100}.",
        "year": year_turn_100
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
