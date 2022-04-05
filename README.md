# Student Exam Performance Prediction

![Project Banner](https://github.com/user-attachments/assets/823a134f-319d-4e08-bb7f-5ca8d7b499bb)

## Overview

This project is an end-to-end machine learning application built using Flask, which predicts the math score of students based on various features like gender, race/ethnicity, parental level of education, lunch type, test preparation course, and scores in reading and writing. The project follows a modular approach with clear separation of concerns, making it easy to maintain and scale.

## Table of Contents

- [Project Structure](#project-structure)
- [Usage](#usage)
- [Data Pipeline](#data-pipeline)
- [Modeling](#modeling)
- [Prediction Pipeline](#prediction-pipeline)
- [Results](#results)
- [Screenshots](#screenshots)
- [About Me](#-about-me)
- [Contact](#contact)

## Project Structure

```bash
├── app.py
├── src
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline
│   │   ├── predict_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
├── templates
│   ├── index.html
│   ├── home.html
├── README.md
├── requirements.txt
└── logs
```

## Usage

1. Go to the homepage and navigate to the prediction form.
2. Fill in the required student details such as gender, ethnicity, parental education level, etc.
3. Click on "Predict your Maths Score" to get the predicted score.

## Data Pipeline

### Data Ingestion

- **Source:** The data is read from a CSV file.
- **Processing:** The dataset is split into training and testing sets.

### Data Transformation

- **Numerical Features:** Imputation of missing values and scaling.
- **Categorical Features:** Imputation, encoding, and scaling.

### Model Training

- **Models:** Various regression models like Random Forest, Gradient Boosting, etc.
- **Evaluation:** The models are evaluated using R² score and the best model is selected.

## Prediction Pipeline

The prediction pipeline includes loading the trained model and preprocessing objects to transform new data and make predictions.

## Results

Here are some visualizations and results from the project:

### Model Performance Comparison

![Model Performance Comparison](https://github.com/user-attachments/assets/c62a90ca-fffb-4f7b-a0c7-365d5feded4b)

This screenshot of logs shows the performance metrics (e.g., R² score, RMSE, MAE) of all the training algorithms used in the project.

### Prediction Example

![Prediction Example](https://github.com/user-attachments/assets/b4640d5b-ad7d-42eb-834a-5c2f79454ce3)

## Screenshots

### Homepage

![Homepage](https://github.com/user-attachments/assets/0c5b7714-279e-4159-8ae5-b7511a44222a)

### Prediction Page

![Prediction Page](https://github.com/user-attachments/assets/65d80e55-731f-44a1-ac31-2896e4b35366)

## 🚀 About Me

Hello, I'm Akhilesh Thapliyal! 👋
## Contact

- **Email:** akhilesh.thedev@gmail.com
- **LinkedIn:** www.linkedin.com/in/akhilesh-thapliyal
- **GitHub:** https://github.com/The-Akhilesh-Thapliyal
