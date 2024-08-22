from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('pipeline_rf.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a route for the index (homepage)
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    gender = request.form['gender']
    age = float(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    duration = float(request.form['duration'])
    heart_rate = float(request.form['heart_rate'])
    body_temp = float(request.form['body_temp'])

    # Prepare input data as a DataFrame
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp],
    })

    # Predict with the model
    predicted_calories = model.predict(input_data)[0]

    # Return result as JSON
    return jsonify({'result': predicted_calories})

if __name__ == '__main__':
    app.run(debug=True)
