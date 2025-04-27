from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'prices.json'

# Load prices from file
def load_prices():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save prices to file
def save_prices(prices):
    with open(DATA_FILE, 'w') as f:
        json.dump(prices, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_prices')
def get_prices():
    prices = load_prices()
    return jsonify(prices)

@app.route('/save_price', methods=['POST'])
def save_price():
    data = request.get_json()
    date = data['date']
    price = data['price']
    
    prices = load_prices()
    prices[date] = price
    save_prices(prices)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
