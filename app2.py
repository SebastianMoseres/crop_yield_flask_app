from flask import Flask, request, render_template
import pandas as pd
import joblib
import os
import pickle

# Initialize the Flask application
app = Flask(__name__)

# Load the trained machine learning model safely
model_path = os.path.join(os.path.dirname(__file__), 'crop_yield_model.pkl')
print(f"Loading model from {model_path}")

try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"Joblib failed to load the model: {e}")
    print("Attempting to load with pickle instead...")
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

# Define the main route for the web application
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ''
    if request.method == 'POST':
        # Get the data from the form
        form_data = request.form.to_dict()
        
        # Convert data types for the model
        form_data['Rainfall_mm'] = float(form_data['Rainfall_mm'])
        form_data['Temperature_Celsius'] = float(form_data['Temperature_Celsius'])
        form_data['Days_to_Harvest'] = int(form_data['Days_to_Harvest'])
        # The model's pipeline expects boolean or int for these
        form_data['Fertilizer_Used'] = True if form_data['Fertilizer_Used'] == 'True' else False
        form_data['Irrigation_Used'] = True if form_data['Irrigation_Used'] == 'True' else False

        # Create a DataFrame from the form data
        # The column order must match the order the model was trained on
        input_df = pd.DataFrame([form_data])

        # Make a prediction
        prediction = model.predict(input_df)

        # Format the prediction text to display on the page
        prediction_text = f'Predicted Crop Yield: {prediction[0]:.2f} tons per hectare'

    # Render the HTML page, passing the prediction text to it
    return render_template('index.html', prediction_text=prediction_text)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)