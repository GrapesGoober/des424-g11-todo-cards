from fastapi import FastAPI
from pydantic import BaseModel
import database

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

class RecordTextBody(BaseModel):
    text: str

@app.post("/api/record/")
async def record(body: RecordTextBody):
    database.record_text_to_db(body.text)
    body.text = "got " + body.text
    return body

# NOTE: this is just an example API
# feel free to rewrite classes and design it as much as you wish
from user.user import SignUp

@app.post("/api/user/create")
async def create(body: SignUp.RequestBody):
    return SignUp.sign_up(body)