import os
from utils.model_loader import ModelLoader
from exceptions.custom_exceptions import DocumentPortalException
from logger.custom_logging import CustomLogger
from models.model import *
from langchain.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
import sys
from promt.prompt_library import *

class DocumnetAnalyszer:
    def __init__(self):
        
        self.log= CustomLogger.get_logger(__name__)
        try:
            self.loader = ModelLoader()
            self.llm=self.loader.load_llm()
            
            self.parser = JsonOutputParser(pydantic_object = Metadata)
            self.fixing_parser = OutputFixingParser.from_llm(parser = self.parser,llm = self.llm)
            
            self.prompt = prompt 
            self.log.info("DocumentAnalyser init successfully")
        except Exception as e:
            self.log.error("Error initializing DocumentAnalyser: {e}")
            raise DocumentPortalException("Error in initialization",sys)
            
    def analyze_metadata(self):
        pass