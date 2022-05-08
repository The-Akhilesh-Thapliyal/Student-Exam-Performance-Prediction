# Student Exam Performance Prediction

![Project Banner](https://github.com/user-attachments/assets/823a134f-319d-4e08-bb7f-5ca8d7b499bb)

## Overview

This project is an end-to-end machine learning application built using Flask, which predicts the math score of students based on various features like gender, race/ethnicity, parental level of education, lunch type, test preparation course, and scores in reading and writing. The project follows a modular approach with clear separation of concerns, making it easy to maintain and scale.

## Table of Contents

- [Project Structure](#project-structure)
- [Usage](#usage)
- [Data Pipeline](#data-pipeline)
- [Prediction Pipeline](#prediction-pipeline)
- [AWS Deployment](#aws-deployment)
- [Results](#results)
- [Screenshots](#screenshots)
- [About Me](#-about-me)
- [Contact](#contact)

## Project Structure

```bash
├── application.py
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

## AWS Deployment

The project is deployed on AWS using Elastic Beanstalk for scalable web app deployment. Below are the key steps and a few visuals illustrating the deployment:

1. **Continuous Deployment Pipeline**: The project uses AWS CodePipeline to automatically deploy new versions of the app whenever changes are pushed to the repository.

   ![Continuous Deployment Pipeline](https://github.com/user-attachments/assets/a93bcb74-5ff8-48fd-8b5f-7e226639d574)


3. **Homepage of the Web App in AWS**: This is the landing page for the deployed web app hosted on AWS Elastic Beanstalk.

   ![Homepage AWS](https://github.com/user-attachments/assets/aafb72b1-3c7f-4f88-9406-23742aa7867b)


5. **Student Exam Performance Prediction Page on AWS**: This is the page where users input student data and get predictions for math scores.
   
   ![Prediction Page AWS](https://github.com/user-attachments/assets/b0d12828-0981-4aa2-8cd4-2d4669287efd)


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
