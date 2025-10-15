🌾 Agriculture Crop Yield Prediction App
![alt text](https://img.shields.io/badge/python-3.9+-blue.svg)
![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)
An interactive web application that predicts agricultural crop yield based on environmental and farming inputs. This tool uses a powerful machine learning model trained on a dataset of 1 million samples to provide real-time predictions.
📸 Screenshot
(Replace this with a screenshot of your running Streamlit app!)
✨ Features
Interactive Interface: Use sliders and dropdowns to easily input various agricultural parameters.
Real-Time Predictions: Get an instant prediction for crop yield (in tons per hectare) based on your inputs.
High-Accuracy Model: Powered by a Random Forest Regressor model with a proven high R² score of 0.91 on test data.
Data-Driven Insights: Helps users understand how different factors like rainfall, temperature, and fertilizer usage can impact crop productivity.
🛠️ Technology Stack
Language: Python
Machine Learning: Scikit-learn, Pandas
Web Framework: Streamlit
Data Visualization: Matplotlib, Seaborn
Model Persistence: Joblib
⚙️ Installation & Usage
To run this application on your local machine, please follow these steps:
1. Clone the Repository
code
Bash
git clone https://github.com/your-username/crop-yield-prediction.git
cd crop-yield-prediction
2. Create and Activate a Virtual Environment (Recommended)
For macOS/Linux:
code
Bash
python3 -m venv venv
source venv/bin/activate
For Windows:
code
Bash
python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies
Create a file named requirements.txt and add the following libraries to it:
code
Code
streamlit
pandas
scikit-learn==<your_sklearn_version> # e.g., 1.3.0
joblib
Then, install them using pip:
code
Bash
pip install -r requirements.txt```

**4. Run the Streamlit App**

Make sure your trained model file (`crop_yield_model.pkl`) is in the same directory as the app script.

```bash
streamlit run app.py
Your web browser will automatically open with the application running!
🔬 Project Methodology
The prediction model was developed following a standard machine learning workflow:
Exploratory Data Analysis (EDA): The dataset was analyzed to understand feature distributions and correlations. Key insights included the strong positive correlation between Rainfall_mm and Yield, and the approximately normal distribution of the crop yield.
Data Preprocessing: Categorical features (Region, Soil_Type, etc.) were converted into a numerical format using One-Hot Encoding. Boolean features were converted to integers (0/1).
Model Training: A Random Forest Regressor was chosen for its high accuracy on tabular data and its ability to capture complex, non-linear relationships. The model was trained on 80% of the dataset.
Model Evaluation: The model's performance was validated on a 20% hold-out test set to ensure it generalizes well to new, unseen data.
📊 Model Performance
The final model achieved the following performance on the test set:
R-squared (R²): 0.91
(This means the model can explain 91% of the variance in crop yield.)
Mean Absolute Error (MAE): 0.41 tons/hectare
(On average, the model's prediction is off by only 0.41 tons per hectare.)
Mean Squared Error (MSE): 0.27
🚀 Future Improvements
Optimization Mode: Add a feature to find the optimal crop type and conditions for a user's specific, unchangeable inputs (like Region and Soil Type).
Prediction Explanation: Integrate SHAP or LIME to explain why the model made a particular prediction, increasing trust and transparency.
Deployment: Deploy the application to a cloud service (like Streamlit Community Cloud or Heroku) to make it publicly accessible.
📜 License
This project is distributed under the MIT License. See the LICENSE file for more information.
👨‍💻 Author
(SebastianMoseres) - https://github.com/SebastianMoseres