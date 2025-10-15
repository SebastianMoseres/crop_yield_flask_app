from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('crop_yield_model.pkl')

@app.route('/')
def home():
    # Just render the initial HTML page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data sent from the JavaScript
    json_data = request.get_json(force=True)
    
    # The JSON data is already a dictionary, so we can pass it to DataFrame
    input_df = pd.DataFrame([json_data])

    # Convert data types just like before, but from the JSON data
    input_df['Rainfall_mm'] = pd.to_numeric(input_df['Rainfall_mm'])
    input_df['Temperature_Celsius'] = pd.to_numeric(input_df['Temperature_Celsius'])
    input_df['Days_to_Harvest'] = pd.to_numeric(input_df['Days_to_Harvest'])
    input_df['Fertilizer_Used'] = input_df['Fertilizer_Used'].astype(bool)
    input_df['Irrigation_Used'] = input_df['Irrigation_Used'].astype(bool)

    # Make prediction
    prediction = model.predict(input_df)

    # Return the prediction as a JSON object
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)