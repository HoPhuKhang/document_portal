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
        return logging.getLogger(name)
    
if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    logger.info("Logging has started")
                            
        