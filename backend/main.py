from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow React(Port 3000) interact with FastAPI (port 8000)
app.add_middleware(
                    CORSMiddleware,
                   allow_origins=["http://localhost:3000"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):
    return {"reply": f"You said: '{message.text}'. backend is connected! "}