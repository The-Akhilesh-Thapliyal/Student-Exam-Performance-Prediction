import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    Function to extract and format the error message along with the traceback details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: {file_name} at line number: {exc_tb.tb_lineno} - Error Message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom Exception class to capture detailed error messages.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        """
        String representation of the error message.
        """
        return self.error_message
