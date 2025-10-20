

import os
import sys
from dotenv import load_dotenv
from utils.config_loader import load_config
from logger.custom_logging import CustomLogger
from exception.custom_exception import DocumentPortalException

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

log = CustomLogger().get_logger(__name__)

class ModelLoader:
    def __init__(self):
        load_dotenv()
        self.config = load_config()
        self._validate_env()
        log.info("Environment variables loaded successfully.")

    def _validate_env(self):
        required_vars = ['GOOGLE_API_KEY', 'GROQ_API_KEY']
        self.api_keys = {key: os.getenv(key) for key in required_vars}

        missing_vars = [key for key, value in self.api_keys.items() if not value]
        if missing_vars:
            log.error(f"Missing required environment variables: {', '.join(missing_vars)}")
            # Không có exception cũ, nên sys.exc_info() rỗng
            raise DocumentPortalException(
                f"Missing required environment variables: {', '.join(missing_vars)}",
                sys
            )
        log.info("Environment variables validated.")

    def load_embeddings(self):
        try:
            log.info("Loading Google Generative AI Embeddings model...")
            model_name = self.config['embedding_model']['model_name']
            return GoogleGenerativeAIEmbeddings(model=model_name)
        except Exception as e:
            log.error(f"Error loading embeddings model: {e}")
            raise DocumentPortalException(e, sys)

    def load_llm(self):
        llm_block = self.config['llm']
        log.info("Loading LLM model...")

        provider_key = os.getenv("LLM_PROVIDER", "groq")
        if provider_key not in llm_block:
            log.error(f"LLM provider '{provider_key}' not found in configuration.")
            raise DocumentPortalException(f"LLM provider '{provider_key}' not found in configuration.", sys)

        llm_config = llm_block[provider_key]
        provider = llm_config.get('provider')
        model_name = llm_config.get('model_name')
        temperature = llm_config.get('temperature', 0)
        max_tokens = llm_config.get('max_tokens', 1024)

        log.info(f"Selected LLM provider: {provider}, model: {model_name}, temperature: {temperature}, max_tokens: {max_tokens}")

        if provider_key == "groq":
            return ChatGroq(
                model=model_name,
                temperature=temperature,
                max_tokens=max_tokens,
                api_key=self.api_keys['GROQ_API_KEY']
            )
        elif provider_key == "google":
            return ChatGoogleGenerativeAI(
                model=model_name,
                temperature=temperature,
                max_output_tokens=max_tokens,
                api_key=self.api_keys['GOOGLE_GENAI_API_KEY']
            )
        else:
            log.error(f"Unsupported LLM provider: {provider_key}")
            raise DocumentPortalException(f"Unsupported LLM provider: {provider_key}", sys)

if __name__ == "__main__":
    loader = ModelLoader()
    embeddings = loader.load_embeddings()
    result =  embeddings.embed_query("Hello world")
    print("✅ Loaded embeddings model successfully")
    print(result)
