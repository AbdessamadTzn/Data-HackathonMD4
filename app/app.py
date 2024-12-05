from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import joblib
import os

# Load environment variables
load_dotenv()

# Get files from the env
MODEL_PATH = os.getenv("MODEL_PATH")
STATIC_IMAGE_PATH = os.getenv("STATIC_IMAGE_PATH")

# Load the model
model = joblib.load(MODEL_PATH)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', STATIC_IMAGE_PATH=STATIC_IMAGE_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    mntwines = request.form['MntWines']
    income = request.form['Income']
    mntgoldprods = request.form['MntGoldProds']
    customer_age = request.form['Customer_Age']
    recency = request.form['Recency']
    numacceptedcmp = request.form['NumAcceptedCmp']
    mntmeatproducts = request.form['MntMeatProducts']
    
    try:
        # Convert to the appropriate data types (int or float)
        mntwines = float(mntwines)  # Assuming MntWines and other features are numeric
        income = float(income)
        mntgoldprods = float(mntgoldprods)
        customer_age = int(customer_age)  # Assuming age is an integer
        recency = int(recency)  # Recency might be a categorical variable, or an integer
        numacceptedcmp = int(numacceptedcmp)  # Number of accepted campaigns
        mntmeatproducts = float(mntmeatproducts)

        # Prepare the features for prediction
        features = [[mntwines, income, mntgoldprods, customer_age, recency, numacceptedcmp, mntmeatproducts]]
        
        # Make prediction
        prediction = model.predict(features)[0]

        # Return the prediction as a JSON response
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        # In case of an error, return the error message with status code 400
        return jsonify({'error': str(e)}), 400




if __name__ == '__main__':
    app.run()