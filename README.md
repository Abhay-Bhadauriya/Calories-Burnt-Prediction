# Calories Burned Prediction

This project predicts the number of calories burned during exercise based on user input parameters such as gender, age, height, weight, exercise duration, heart rate, and body temperature. The project demonstrates a complete machine learning pipeline, from data preprocessing to model deployment, and provides a graphical user interface (GUI) for easy interaction.

 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [GUI Interaction](#gui-interaction)
- [License](#license)

## Project Overview
The project involves training machine learning models to predict calories burned during exercise. It uses two primary models:
1. Linear Regression
2. Random Forest Regressor

The trained models are evaluated using metrics like R² score and Mean Absolute Error (MAE). The Random Forest model is saved and deployed via a Tkinter-based GUI, allowing users to input their data and receive calorie predictions.

## Features
- **Data Preprocessing**: Handles both categorical and numerical data using encoding and scaling techniques.
- **Model Training and Evaluation**: Trains and evaluates models using cross-validation and performance metrics.
- **Model Persistence**: Saves the trained model using `pickle` for later use.
- **User Interface**: Provides a Tkinter-based GUI for easy interaction with the model.

## Installation

### Prerequisites
- Python 3.7 or higher
- `pip` package manager
