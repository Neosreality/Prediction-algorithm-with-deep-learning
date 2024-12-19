from flask import Flask, request, jsonify
import pandas as pd
from models.model import StockModel
from utils import load_data

app = Flask(__name__)

# Load the stock data
data = load_data('data/stock_data.csv')

# Initialize the stock prediction model
model = StockModel()
model.train(data)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)