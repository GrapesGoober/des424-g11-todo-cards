
from pydantic import BaseModel

class SignUp:
    class RequestBody(BaseModel):
        username: str
        password: str

    class ResponseBody(BaseModel):
        status: bool

    def sign_up(body: RequestBody) -> ResponseBody:
        print(f"signed up with {body.username} and {body.password}")
        return SignUp.ResponseBody(False)

class Login:
    class RequestBody(BaseModel):
        username: str
        password: str

    # technically, we should use OAuth to do this securely,
    # but for the sake of demonstration, do this
    class ResponseBody(BaseModel):
        status: bool

    def login(body: RequestBody) -> ResponseBody:
        print(f"logged in with {body.username} and {body.password}")
        return Login.ResponseBody(False)