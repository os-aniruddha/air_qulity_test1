from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model_path = "model1.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form
        COi = float(data['COi'])
        NOi = float(data['NOi'])
        Temp_AQI = float(data['Temp_AQI'])
        Humidity_AQI = float(data['Humidity_AQI'])

        # Prepare input for the model
        features = np.array([[COi, NOi, Temp_AQI, Humidity_AQI]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Return JSON response
        return jsonify({
            'status': 'success',
            'input': {
                'COi': COi,
                'NOi': NOi,
                'Temp_AQI': Temp_AQI,
                'Humidity_AQI': Humidity_AQI
            },
            'prediction': prediction
        })
    except Exception as e:
        # Handle errors
        return jsonify({'status': 'error', 'message': str(e)})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
