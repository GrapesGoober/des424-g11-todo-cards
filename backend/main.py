from fastapi import FastAPI

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

# @app.post("/api/user/login")
# async def login(body: Login.RequestBody):
#     return Login.login(body)