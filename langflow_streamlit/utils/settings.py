import dotenv
import os

dotenv.load_dotenv()


STREAMLIT_PORT = int(os.getenv("STREAMLIT_PORT", "5001"))

LANGFLOW_PORT = int(os.getenv("LANGFLOW_PORT", "7860"))

API_PORT = int(os.getenv("API_PORT", "7881"))

FOLDER_PATH = os.getenv("FOLDER_PATH", "./")

STREAMLIT_ONLY = os.getenv("STREAMLIT_ONLY", "false").lower() in ["true", "1"]
