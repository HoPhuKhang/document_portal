import sys
import traceback
from logger.custom_logging import CustomLogger
logger = CustomLogger().get_logger("exception")

class DocumentPortalException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        # Lấy thông tin ngoại lệ hiện tại nếu có
        exc_type, exc_value, exc_tb = error_detail.exc_info()

        # Nếu có traceback thực, lấy thông tin chi tiết
        if exc_tb:
            self.file_name = exc_tb.tb_frame.f_code.co_filename
            self.line_number = exc_tb.tb_lineno
            self.tracreback_str = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        else:
            # Nếu không có traceback (vd raise thủ công)
            self.file_name = "N/A"
            self.line_number = "N/A"
            self.tracreback_str = "No active exception traceback."
        
        self.error_message = str(error_message)

    def __str__(self):
        return (
            f"\nError in [{self.file_name}] at line number [{self.line_number}]: "
            f"{self.error_message}\nTraceback:\n{self.tracreback_str}"
        )

if __name__ == "__main__":
    try:
        a = 1 / 0  # Gây ra ZeroDivisionError
        print(a)
    except Exception as e:
        app_exc = DocumentPortalException(str(e), sys)
        logger.error(app_exc)
        raise app_exc
