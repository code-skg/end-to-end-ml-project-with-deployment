# here we will handel the eroor occured in our code . 
import sys

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = (
        "Error occurred in python script name [{0}] "
        "line number [{1}] "
        "error message [{2}]"
    ).format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message

    """What this code does (simple explanation)
            When an error happens:

            Captures file name

            Captures line number

            Captures actual error message

            Wraps it in a clean, readable format
    """