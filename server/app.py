from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) 

# Load the model
model_path = 'C:\\Users\\jatin\\Downloads\\HEART-DISEASE-main\\models\\svm_model.pkl'  # Update this with your model path
model = pickle.load(open(model_path, 'rb'))

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract parameters from the request
    Bmi = float(data['BMI'])
    Age = int(data['Age'])
    Sbp = int(data['Systolic Blood Pressure'])
    Dbp = int(data['Diastolic Blood Pressure'])

    # Make prediction using the loaded model
    prediction = model.predict([[Bmi, Age, Sbp, Dbp]])

    # Return the prediction as JSON response
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
