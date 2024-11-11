from datetime import date
from pydantic import BaseModel
from user_function import *

class SignUp:
    class RequestBody(BaseModel):
        username: str
        password: str
        confirm_password: str
        dateOfBirth: date #YYYY-MM-DD
        email: str
        

    class ResponseBody(BaseModel):
        status: bool

    def sign_up(body: RequestBody) -> ResponseBody:
        #check username is exist
        if Is_username_exists(body.username):
            return SignUp.ResponseBody(status=False)

        #check password is the same as confirm_password
        if body.password != body.confirm_password:
            return SignUp.ResponseBody(status=False)
        
        # sing-up complete, update status
        return SignUp.ResponseBody(status=True)
    


class Login:
    class RequestBody(BaseModel):
        username: str
        password: str

    # technically, we should use OAuth to do this securely,
    # but for the sake of demonstration, do this
    class ResponseBody(BaseModel):
        status: bool

    def login(body: RequestBody) -> ResponseBody:
        # verify
        if user_login(body.username, body.password):
            return Login.ResponseBody(status=True)
        else:
            return Login.ResponseBody(status=False)
        

        
