from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from app.core.config import settings
from app.services.weather_tool import get_weather

llm = ChatGroq(
    model=settings.GROQ_MODEL,
    api_key=settings.GROQ_API_KEY
)

# Agent setup
tools = [get_weather]
weather_agent = create_react_agent(llm, tools)

async def run_weather_agent(question: str):
    response = await weather_agent.ainvoke({"messages": [("user", question)]})
    return response["messages"][-1].content