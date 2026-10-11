from flask import Flask, render_template, request
import pickle
import numpy as np
import random

app = Flask(__name__) 

# Load trained model
model = pickle.load(open('diabetes_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    try:
        data = [float(x) for x in request.form.values()]
        pred = model.predict([data])[0]
        result = "🩸 Diabetes Detected" if pred == 1 else "✅ No Diabetes Detected"
        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
