from fastapi import FastAPI
from pydantic import BaseModel
from user.user import SignUp
from user.user import Login

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

import record_text

@app.post("/api/record/")
async def record(body: record_text.RecordTextBody):
    return record_text.record(body)

# NOTE: this is just an example API
# feel free to rewrite classes and design it as much as you wish

@app.post("/api/user/signUp")
async def create(body: SignUp.RequestBody):
    return SignUp.sign_up(body)

@app.post("/api/user/login")
async def create(body: Login.RequestBody):
    return Login.login(body)