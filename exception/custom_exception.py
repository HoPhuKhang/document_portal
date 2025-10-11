import sys
import traceback
from logger.custom_logging import CustomLogger
logger = CustomLogger().get_logger("exception") 

class DocumentPortalException(Exception):
    def __init__(self, error_message:str,error_detail:sys):
        _,_,exc_tb=error_detail.exc_info() # tra ve 3 gia tri (exc_type, exc_value, exc_traceback)
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.line_number=exc_tb.tb_lineno
        self.error_message = str(error_message) 
        self.tracreback_str ="".join(traceback.format_exception(*error_detail.exc_info())) # *error_detail.exc_info() giải nén 3 giá trị: (exc_type, exc_value, exc_tb).       
        
        

    def __str__(self):
        return f"""
        Error in [{self.file_name}] at line number [{self.line_number}] : {self.error_message} \n Traceback : {self.tracreback_str}"""
    
if __name__ == "__main__":
    try:
        a = 1 / 0
        print(a)
    except Exception as e:
        app_exc = DocumentPortalException(str(e),sys)
        logger.error(app_exc)
        raise app_exc