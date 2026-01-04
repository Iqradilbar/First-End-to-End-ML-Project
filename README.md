Student Math Score Prediction System
Overview

The Student Math Score Prediction System is an end-to-end Machine Learning web application that predicts a student’s Math exam score based on multiple academic and demographic factors.
The system is designed using a modular ML pipeline and provides predictions through a Flask-based web interface.

Project Description

Student performance in Mathematics depends on various factors such as:

Gender

Parental level of education

Lunch type

Test preparation course

Reading and writing scores

This project uses these features to predict the Math score accurately using a trained machine learning model.

Objectives

Analyze factors affecting Math performance

Build a reliable ML model for Math score prediction

Implement a clean ML pipeline (ingestion → transformation → training)

Serve predictions through a web-based interface

Follow industry-standard project structure and logging practices

Key Features

Math score prediction based on multiple input features

End-to-end machine learning pipeline

Serialized model and preprocessing artifacts

Flask-based web application

Centralized logging and exception handling

Notebook-based EDA and experimentation

Technologies Used
Machine Learning & Backend

Python

Pandas

NumPy

Scikit-learn

CatBoost

Pickle

Web

Flask

HTML5

Project Structure
Student-Exam-Performance/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── raw.csv
│   ├── train.csv
│   ├── test.csv
│   └── catboost_info/
│
├── logs/
│
├── notebook/
│   ├── EDA_Student_performance.ipynb
│   ├── Model_training.ipynb
│   └── stud.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   └── pipeline/
│       ├── exception.py
│       ├── logger.py
│       └── utils.py
│
└── README.md

Workflow
1. Data Ingestion

Reads raw student data

Splits data into training and testing sets

Stores datasets in the artifacts/ directory

2. Data Transformation

Handles categorical and numerical features

Applies preprocessing and feature engineering

Saves the preprocessor as preprocessor.pkl

3. Model Training

Trains a Math score prediction model using CatBoost

Saves the trained model as model.pkl

4. Prediction

User enters student details via the web interface

Model predicts the Math score

Result is displayed on the web page

How to Run the Project
Install Dependencies
pip install -r requirements.txt

Run Flask Application
python app.py


Open browser:

http://127.0.0.1:5000/

Dataset

The dataset contains student information including:

Gender

Parental education

Lunch type

Test preparation status

Reading score

Writing score

The target variable is Math score.

Future Improvements

Display prediction confidence

Add data visualization on UI

Improve UI/UX design

Deploy on cloud platform

Add REST API support

Author

Iqra Dilbar
BS Artificial Intelligence
Machine Learning Engineer (Aspiring)

Iqra Dilbar
BS Artificial Intelligence
Machine Learning Engineer (Aspiring)
