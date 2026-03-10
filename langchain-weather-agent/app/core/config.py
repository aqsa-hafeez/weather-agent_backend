import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"

settings = Settings()