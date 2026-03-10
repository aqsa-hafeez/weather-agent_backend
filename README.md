# Weather Agent (AI-Powered)

This is a production-ready **AI Weather Agent** built with **FastAPI**, **LangChain**, and **Groq (Llama-3.3-70b)**. It can understand natural language queries and fetch real-time weather data for multiple cities using the OpenWeatherMap API.

---

### 🚀 Features

* **Natural Language Processing:** Uses Groq's Llama-3 model to extract city names and intent.
* **Multi-City Support:** Can fetch weather for multiple cities in a single prompt.
* **FastAPI Backend:** High-performance asynchronous API endpoints.
* **LangGraph Integration:** Uses ReAct agent logic for tool calling.
* **Hugging Face Ready:** Fully compatible with Hugging Face Spaces (Dockerized).

---

### 📂 Project Structure

```text
weather_api/
├── app/
│   ├── core/         # Config and API keys
│   ├── models/       # Pydantic Schemas
│   ├── services/     # Weather Tool & Agent Logic
│   ├── routes/       # FastAPI Endpoints
│   └── main.py       # Entry Point
├── Dockerfile        # Deployment configuration
├── README.md         # Documentation
└── requirements.txt  # Dependencies

```

---

### 🛠️ Setup Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/Hafeezaqsa01/Weather_agent.git
cd Weather_agent

```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

#### 3. Environment Variables

Create a `.env` file in the root directory and add your keys:

```env
OPENWEATHER_API_KEY=your_openweather_key_here
GROQ_API_KEY=your_groq_key_here

```

#### 4. Run Locally

```bash
uvicorn app.main:app --reload

```

Visit `http://127.0.0.1:8000/docs` to test the API.

---


### 📡 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Health check / Status |
| `POST` | `/api/v1/ask` | Send a weather question to the AI agent |

**Example Request:**

```json
{
  "question": "What's the weather like in London and Tokyo?"
}

```

---

### 🧰 Tech Stack

* **LLM:** Groq (Llama-3.3-70b)
* **Framework:** FastAPI
* **Orchestration:** LangChain / LangGraph
* **Deployment:** Docker / Hugging Face Spaces

---
