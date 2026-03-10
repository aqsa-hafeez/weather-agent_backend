from fastapi import FastAPI
from app.routes import weather

# 1. Tags ki metadata define karein taake order fix ho jaye
tags_metadata = [
    {
        "name": "General",
        "description": "API status and health check endpoints.",
    },
    {
        "name": "Weather",
        "description": "AI-powered weather agent endpoints.",
    },
]

app = FastAPI(
    title="Weather Agent API",
    openapi_tags=tags_metadata  # Yahan order define hota hai
)

# 2. Root endpoint ko "General" tag dein taake wo "default" se nikal kar upar aa jaye
@app.get("/", tags=["General"])
def read_root():
    return {"message": "Weather Agent is online!"}

# 3. Weather router pehle se hi "Weather" tag ke saath hai
app.include_router(weather.router, tags=["Weather"])