import os
import utils.model_loader import ModelLoader
from exceptions.custom_exceptions import DocumentPortalException
from logger.custom_logging import CustomLogger
from models.model import *
from langchain.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser


class DocumnetAnalyszer:
    def __init__(self):
        pass
    def analyze_metadata(self):
        pass