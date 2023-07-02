# Any exception that is getting controlled, sys library will have that information 
import sys
import logging

def error_message_detail(error, error_detail:sys):
    # All information about the exception is stored in the variable
    _, _, exc_tb = error_detail.exc_info()

    # Extract the file name from exc_info 
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "ERROR OCCURED IN PYTHON SCRIPT NAME[{0}], LINE NUMBER [{1}], ERROR MESSAGE: [{2}]".format(file_name, exc_tb.tb_lineno, str(error) )

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message()

