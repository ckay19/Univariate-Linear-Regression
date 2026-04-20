import pandas as pd
import pickle
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

fileObj = open('model.obj', 'rb')
model = pickle.load(fileObj)

@app.route("/")
def index():
    return render_template('sample.html')

@app.route("/submit", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        study_hours = request.form.get('Study hours')
        if study_hours:
            try:
                study_hours = float(study_hours)
                # Perform prediction
                prediction = model.predict([[study_hours]])
                # Map prediction to human-readable label
                liked_label = f"Predicted Score: {prediction[0]:.2f}%"
                return render_template('sample.html', liked=liked_label, show_result=True)
            except ValueError:
                return render_template('sample.html', liked="Invalid input. Please enter a number.", show_result=True)
        else:
            return render_template('sample.html', liked="Please enter the study hours.", show_result=True)
    else:
        # Handle GET request
        return render_template('sample.html', show_result=False)

if __name__ == '__main__':
    app.run(debug=True)
