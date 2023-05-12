import sys
from src.logger import logging

def error_message(error,error_detail:sys)->str:
    _,_,exe_tb=error_detail.exc_info()
    filename = exe_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(filename, exe_tb.tb_lineno, str(error)
    )
    return error_message


class CustomeException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message(error_message, error_detail=error_detail)