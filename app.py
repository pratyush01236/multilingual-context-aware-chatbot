from fastapi import FastAPI
from pydantic import BaseModel
from chatbot.engine import ChatEngine
app=FastAPI(title="Multilingual Context-Aware Chatbot",version="1.0.0")
engine=ChatEngine()
class ChatRequest(BaseModel):
    customer_id:str
    message:str
@app.get("/")
def health(): return {"status":"ok","features":["multilingual","mixed-language","session-isolation","context","expiry"]}
@app.post("/chat")
def chat(req:ChatRequest): return engine.reply(req.customer_id,req.message)
