from pydantic import BaseModel, Field


class ChatMessageModel(BaseModel):
    role: str
    content: str
    type: str = Field("text", pattern="text|image")
