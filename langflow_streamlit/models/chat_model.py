from typing import Optional
from pydantic import BaseModel
from langflow_streamlit.utils import settings


class ChatModel(BaseModel):
    title: str = "Welcome to My Streamlit Chat Application"
    welcome_msg: str = "Hello human, welcome to the digital world. Feel free to ask questions; I am ready to help you."
    write_speed: float = 0.05
    input_msg: str = "Ask some question..."
    ai_avatar: Optional[str] = None
    user_avatar: Optional[str] = None
    port: int = settings.STREAMLIT_PORT
