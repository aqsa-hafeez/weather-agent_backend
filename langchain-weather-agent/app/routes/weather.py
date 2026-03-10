from fastapi import APIRouter, HTTPException
from app.models.schemas import WeatherRequest, WeatherResponse
from app.services.agent_logic import run_weather_agent

router = APIRouter()

@router.post("/ask", response_model=WeatherResponse)
async def ask_weather(payload: WeatherRequest):
    try:
        answer = await run_weather_agent(payload.question)
        return WeatherResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))