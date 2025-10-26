import os
import sys
import fitz 
import uuid 
from datetime import datetime
from logger.custom_logging import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentHander:
    def __init__(self,data_dir = None,session_id = None):
        try:
            self.log = CustomLogger().get_logger(__name__)
            self.data_dir = data_dir or os.getenv(
                                "DATA_STORAGE_PATH",
                                os.path.join(os.getcwd(),"data","document_analysis"))
            self.session_id = session_id or f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(uuid.uuid4())[:8]}"
            self.session_path = os.path.join(self.data_dir,self.session_id)
            os.makedirs(self.session_path,exist_ok=True)
            self.log.info(f"Initialized DocumentHandler with session ID: {self.session_id}")
        except Exception as e:
            self.log.error(f"Error initializing DocumentHandler: {str(e)}")
            raise DocumentPortalException(f"Initialization failed: {str(e)}")
        
        pass
    def save_pdf(self,upload_file):
        try:
            filename = os.path.basename(upload_file.name)
            
            if not filename.lower().endswith(".pdf"):
                raise DocumentPortalException("Invalid file type.Only PDF are allowed")
            save_path = os.path.join(self.session_path,filename)
            with open(save_path,"wb") as f:
                f.write(upload_file.getbuffer())
            return save_path

        except Exception as e:
            self.log.error(f"Error saving PDF: {str(e)}")
            raise DocumentPortalException(f"Saving PDF failed: {str(e)}")   
    def read_pdf(self,pdf_path):
        try:
            text_chunk = []
            with fitz.open(pdf_path) as doc:
                for page_num,page in enumerate(doc,start= 1):
                    text_chunk.append(f"\n ---page {page_num} ---\n{page.get_text()}")
            text = "\n".join(text_chunk)
            self.log.info(f"PDF read successfully: {pdf_path}, session_id={self.session_id}, pages={len(text_chunk)}")
            return text
        except Exception as e:
            self.log.error(f"Error reading PDF: {e}")
            raise DocumentPortalException("Error reading PDf",e) from e 
    
if __name__ == "__main__":
    from pathlib import Path
    from io import BytesIO
    
    pdf_path = "/Users/hophukhang/document_portal/notebook/data/sample.pdf"
    
    class DummyFile:
        def __init__(self,file_path):
            self.name = Path(file_path).name
            self.file_path = file_path
        def getbuffer(self):
            return open(self.file_path,"rb").read()
            
            
    dummy = DummyFile(pdf_path)
    handler = DocumentHander(session_id="test_session")
    try:
        save_path = handler.save_pdf(dummy)
        print(save_path)
        print("PDF content")
        content = handler.read_pdf(save_path)
        print(content)
    except Exception as e:
        print(e)
        
    