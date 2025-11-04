import os
from pydantic import BaseModel

class Settings(BaseModel):
    PROJECT_NAME: str = "Braughing Loccoli API"
    VERSION: str = "1.0.0"
    BACKEND_CORS_ORIGINS: list[str] = ["http://127.0.0.1:5173","http://localhost:5173"]  # or restrict later
    API_PREFIX: str = "/api"
    PORT: int = 9002
    HOST: str = "0.0.0.0"

settings = Settings()
