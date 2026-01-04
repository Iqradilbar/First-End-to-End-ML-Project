from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipline.predict_pipline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Get all form values
        gender = request.form.get('gender')
        ethnicity = request.form.get('ethnicity')
        parental_education = request.form.get('parental_level_of_education')
        lunch = request.form.get('lunch')
        test_prep = request.form.get('test_preparation_course')
        reading = request.form.get('reading_score')
        writing = request.form.get('writing_score')
        
        # Validate that all fields are filled
        if not all([gender, ethnicity, parental_education, lunch, test_prep, reading, writing]):
            return render_template('home.html', results="Error: Please fill all fields!")
        
        data = CustomData(
            gender=gender,  
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_education,
            lunch=lunch,
            test_preparation_course=test_prep,
            reading_score=float(reading),
            writing_score=float(writing)
        )
        
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Data types:", pred_df.dtypes)
        print("Null values:", pred_df.isnull().sum())

        predict_pipline = PredictPipeline()
        results = predict_pipline.predict(pred_df)
        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)