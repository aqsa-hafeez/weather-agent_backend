from pydantic import BaseModel

class WeatherRequest(BaseModel):
    question: str

class WeatherResponse(BaseModel):
    answer: str