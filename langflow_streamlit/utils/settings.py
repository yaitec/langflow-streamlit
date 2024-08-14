import dotenv
import os

dotenv.load_dotenv()


LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

GENERATE_LOG_FILE = os.getenv("GENERATE_LOG_FILE", "false").lower() in ["1", "true"]

LANGFLOW_STARTUP_TIMEOUT = os.getenv("LANGFLOW_STARTUP_TIMEOUT", "20")

STREAMLIT_PORT = int(os.getenv("STREAMLIT_PORT", "5001"))

LANGFLOW_PORT = int(os.getenv("LANGFLOW_PORT", "7860"))

API_PORT = int(os.getenv("API_PORT", "7881"))

FOLDER_PATH = os.getenv("FOLDER_PATH", "./")

STREAMLIT_ONLY = os.getenv("STREAMLIT_ONLY", "false").lower() in ["true", "1"]

if LANGFLOW_STARTUP_TIMEOUT.isdigit():
    LANGFLOW_STARTUP_TIMEOUT = int(LANGFLOW_STARTUP_TIMEOUT)
else:
    raise Exception("The LANGFLOW_STARTUP_TIMEOUT environment variable must be a valid integer")
