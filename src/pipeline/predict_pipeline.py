import sys
import pandas as pd
import os
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass  # Initialize without any arguments, serves as a placeholder for future initialization if needed.

    def predict(self, features):
        """
        Predicts the target value based on the input features using a pre-trained model and preprocessor.
        """
        try:
            # Define paths to the saved model and preprocessor objects
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            # Loading the model and preprocessor
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Transform the input features using the preprocessor
            data_scaled = preprocessor.transform(features)

            # Make predictions using the trained model
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            # Raise a custom exception if something goes wrong
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, gender: str, race_ethnicity: str, parental_level_of_education, lunch: str, 
                 test_preparation_course: str, reading_score: int, writing_score: int):
        """
        Initialize the CustomData object with the necessary features.
        """
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        """
        Converts the custom data into a pandas DataFrame for prediction.
        """
        try:
            # Creating a dictionary with the provided data
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            # Returning the dictionary as a pandas DataFrame
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            # Raise a custom exception if something goes wrong
            raise CustomException(e, sys)
