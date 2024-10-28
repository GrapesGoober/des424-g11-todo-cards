from fastapi import FastAPI
from pydantic import BaseModel
import backend.database as database

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

class PingBody(BaseModel):
    text: str

@app.post("/api/ping/")
async def ping(body: PingBody):
    body.text = "got " + body.text
    return body

@app.post("/api/database/")
async def ping(body: PingBody):
    database.record_to_db(body.text)
    return True