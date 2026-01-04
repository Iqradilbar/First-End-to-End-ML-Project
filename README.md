# Student Math Score Prediction System

## Overview

The **Student Math Score Prediction System** is an end-to-end **Machine Learning web application** that predicts a student’s **Math exam score** based on multiple academic and demographic factors.

The project follows a modular, production-style architecture and provides predictions through a **Flask-based web interface**.


---

## Project Description

Student performance in Mathematics is influenced by various factors such as:

- Gender  
- Parental level of education  
- Lunch type  
- Test preparation course  
- Reading score  
- Writing score  

This system uses these features to **predict the Math score** using a trained machine learning model.


---

## Objectives

- Identify key factors affecting Math performance  
- Build a reliable ML model for Math score prediction  
- Implement an end-to-end ML pipeline  
- Provide predictions via a web interface  
- Maintain clean, scalable project structure with logging  


---

## Key Features

- Math score prediction based on multiple inputs  
- End-to-end ML pipeline (ingestion, transformation, training)  
- Saved model and preprocessor artifacts  
- Flask-based web application  
- Centralized logging and exception handling  
- Jupyter notebooks for EDA and experimentation  


---

## Technologies Used

### Machine Learning & Backend

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- CatBoost  
- Pickle  


### Web

- Flask  
- HTML5  


---

## Project Structure

Student-Exam-Performance/
│
├── app.py
├── requirements.txt
│
├── templates/
│ ├── home.html
│ └── index.html
│
├── artifacts/
│ ├── model.pkl
│ ├── preprocessor.pkl
│ ├── raw.csv
│ ├── train.csv
│ ├── test.csv
│ └── catboost_info/
│
├── logs/
│
├── notebook/
│ ├── EDA_Student_performance.ipynb
│ ├── Model_training.ipynb
│ └── stud.csv
│
├── src/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ │
│ └── pipeline/
│ ├── exception.py
│ ├── logger.py
│ └── utils.py
│
└── README.md

---

## Workflow

### Data Ingestion

- Reads raw student data  
- Splits data into training and testing sets  
- Stores outputs in the `artifacts/` directory  


### Data Transformation

- Processes categorical and numerical features  
- Applies preprocessing and feature engineering  
- Saves preprocessor as `preprocessor.pkl`  


### Model Training

- Trains a **Math score prediction model** using CatBoost  
- Saves trained model as `model.pkl`  


### Prediction

- User enters student details via web form  
- Model predicts the **Math score**  
- Result is displayed on the web page  


---

## How to Run the Project

Install dependencies:

Run the Flask application:



python app.py


Open in browser:



http://127.0.0.1:5000/



---

## Dataset

The dataset contains student information including:

- Gender  
- Parental education  
- Lunch type  
- Test preparation status  
- Reading score  
- Writing score  

**Target variable:** Math score


---

## Future Improvements

- Add prediction confidence and metrics  
- Improve UI/UX  
- Add REST API support  
- Deploy on cloud platform  


---

## Author

**Iqra Dilbar**  
BS Artificial Intelligence  


---
