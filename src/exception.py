import sys
import logging

# error message raise it return own CustomException message 
def error_message_detail(error,error_deatails :sys): # step 2- find the error 
    _,_,exc_tb=error_deatails.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message= 'Error ocured python script [{0}] line no [{1}] error message [{2}] '.format(
        file_name,exc_tb.tb_lineno,str(error))
    # step 3- error message details
    
    return error_message
    
#  my own custom exception message.
class CustomException(Exception):
    def __init__(self,error_message,error_deatails: sys):  # step 1- when error occured send error to error_message
        '''
        : patam error message: error message in string format
        '''
        super().__init__(error_message) # step 4- inharite message from message detalis

        self.error_message=error_message_detail(error_message,error_deatails=error_deatails)

    def __str__(self):
        return self.error_message        # final- return error message with where ,when,line no

