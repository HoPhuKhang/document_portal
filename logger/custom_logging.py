import os
import logging
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir = "Loggings"):
        self.log_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.log_dir, self.log_file)
        logging.basicConfig(filename=self.log_file_path,
                            format='[%(asctime)s] %(message)s',
                            level=logging.INFO)
    def get_logger(self, name=__file__):
        logger_name = os.path.basename(name) 
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        file_formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(names) (line:%(lineno)d) - %(message)s')
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setFormatter(file_formatter)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(file_formatter)
        if not logger.handlers:
        
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
        
        return logger
    
if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    logger.info("Logging has started")
                            
        