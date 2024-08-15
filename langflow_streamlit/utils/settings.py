import dotenv
import os

dotenv.load_dotenv()


LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

LOG_FILE_GENERATION = os.getenv("LOG_FILE_GENERATION", "false").lower() in ["1", "true"]

langflow_startup_timeout: str = os.getenv("LANGFLOW_STARTUP_TIMEOUT", "20")

STREAMLIT_PORT = int(os.getenv("STREAMLIT_PORT", "5001"))

LANGFLOW_PORT = int(os.getenv("LANGFLOW_PORT", "7860"))

API_PORT = int(os.getenv("API_PORT", "7881"))

FOLDER_PATH = os.getenv("FOLDER_PATH", "./")

STREAMLIT_ONLY = os.getenv("STREAMLIT_ONLY", "false").lower() in ["true", "1"]

if langflow_startup_timeout.isdigit():
    LANGFLOW_STARTUP_TIMEOUT = int(langflow_startup_timeout)
else:
    raise Exception("The LANGFLOW_STARTUP_TIMEOUT environment variable must be a valid integer")
