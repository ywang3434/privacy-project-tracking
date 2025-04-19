# Tracker Prediction and Visualization System

This system predicts website trackers using machine learning and provides interactive visualizations of tracker data.

## File Structure

project/
├── test/
│ └── 2025-01/  # sample testing dataset
├── train/
│ └── 2024-11/  # sample training dataset
├── model_v3.ipynb # Data preparation and model training notebook
├── app.py # Flask API for model serving
├── tracker3.html # Interactive prediction dashboard
├── feature.csv # the feature importance we get from the first model trained
├── popular_tracker.txt # list of popular trackers we get from historical data
├── sites_trackers_2025_01 a prepared data that can be used in tracker3.html
└── README.md

## Prerequisites

- Python 3.8+
- Jupyter Notebook
- Flask
- scikit-learn
- pandas
- numpy
- joblib
- d3.js (for visualization)

# Data Preparation

Please note that we only submitted the sample dataset because of the data size. You can download full dataset from Ghostery's WhoTracksMe.

# Model Training

jupyter notebook src/model_v3.ipynb

# Start the API server

python app.py

The API will run at http://localhost:5000

# Run the application

python -m http.server 800

Launch http://localhost:8000/tracker3.html in a web browser