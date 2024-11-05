
from pydantic import BaseModel
from datetime import date

class SignUp:
    class RequestBody(BaseModel):
        username: str
        password: str
        confirm_password: str
        dateOfBirth: date #YYYYMMDD
        email: str
        

    class ResponseBody(BaseModel):
        status: bool

    def sign_up(body: RequestBody) -> ResponseBody:
        #check username is exist
        
        #check password is the same as confirm_password
        
        print(f"signed up with {body.username} and {body.password}")
        return SignUp.ResponseBody(status=False)
    

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
        return Login.ResponseBody(status=False)