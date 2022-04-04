import os
import sys
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from src.exception import CustomException
import logging

def save_object(file_path, obj):
    """
    Saves a Python object (like a model or preprocessor) to a file using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluates a dictionary of models using GridSearchCV, and returns a dictionary 
    of performance metrics for each model.
    """
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            # Grid search for hyperparameter tuning
            gs = GridSearchCV(model, para, cv=3, n_jobs=-1, verbose=1)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Predicting and evaluating model performance
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Calculate metrics
            train_rmse = mean_squared_error(y_train, y_train_pred, squared=False)
            train_mae = mean_absolute_error(y_train, y_train_pred)
            train_r2 = r2_score(y_train, y_train_pred)

            test_rmse = mean_squared_error(y_test, y_test_pred, squared=False)
            test_mae = mean_absolute_error(y_test, y_test_pred)
            test_r2 = r2_score(y_test, y_test_pred)

            # Store the metrics in the report
            report[list(models.keys())[i]] = {
                "train_rmse": train_rmse,
                "train_mae": train_mae,
                "train_r2": train_r2,
                "test_rmse": test_rmse,
                "test_mae": test_mae,
                "test_r2": test_r2
            }

        return report
    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    """
    Loads a Python object from a pickle file.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
