import os
import pickle
from flask import Flask, request, jsonify

# ----------------------------
# Initialize Flask app
# ----------------------------
app = Flask(__name__)

# ----------------------------
# Load trained model
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'rf_model.pkl')

try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Error: {MODEL_PATH} not found. Please train the model first.")
    exit()

# ----------------------------
# Prediction endpoint
# ----------------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get JSON input
        # Convert JSON to list of features
        features = [list(data.values())]  # assumes one sample per request
        prediction = model.predict(features)[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})

# ----------------------------
# Run the API
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
