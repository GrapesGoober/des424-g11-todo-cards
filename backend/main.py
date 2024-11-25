from fastapi import FastAPI
import record_text
import user

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/record/")
async def record(body: record_text.RecordTextBody):
    return record_text.record(body)

@app.post("/api/user")
async def sign_up(body: user.SignupRequest) -> bool:
    return user.sign_up(body)

@app.post("/api/token")
async def token(body: user.LoginRequest) -> str:
    return user.generate_token(body)

@app.post("/api/test-token")
async def test_token(token: str) -> str:
    return user.verify_jwt_username(token)