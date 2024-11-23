from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

import record_text

@app.post("/api/record/")
async def record(body: record_text.RecordTextBody):
    return record_text.record(body)

import user

@app.post("/api/user")
async def sign_up(body: user.SignupRequest) -> user.SignupResponse:
    return user.sign_up(body)

@app.post("/api/token")
async def token(body: user.LoginRequest) -> str:
    return user.generate_token(body)

@app.post("/api/test-token")
async def test_token(token: str) -> bool:
    return user.verify_token(token)