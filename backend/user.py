
import mysql.connector
from pydantic import BaseModel
from datetime import date

class SignupRequest(BaseModel):
    username: str
    password: str
    date_of_birth: date #YYYY-MM-DD
    email: str

class LoginRequest(BaseModel):
    username: str
    password: str

class SignupResponse(BaseModel):
    status: bool
    message: str = ""

class LoginResponse(BaseModel):
    status: bool

def connect_to_db() -> mysql.connector.MySQLConnection:
    """
    Returns mysql connection to `interns_db` as root user.
    """
    # these configs are defined in compose.yaml
    return mysql.connector.connect(
        host="mysql", # connects to mysql container, instead of normally via "localhost"
        user="root",
        password="",
        database="todocards"
    )

def sign_up(body: SignupRequest) -> SignupResponse:
    """
    Creates a new user into database. 
    If user already exists, returns status `False`.
    Otherwise, returns status `True`.
    """
    db = connect_to_db()
    cursor = db.cursor()

    # Check Username Exists
    cursor.execute("""
        SELECT 
            1 
        FROM 
            `users` 
        WHERE 
            `username` = %(username)s;
    """, body.model_dump())

    if cursor.fetchone() is not None:
        return SignupResponse(
            status=False,
            message="Username already exists"
        )
    
    # Check username length not exceed 20 (defined sized in init.sql)
    if len(body.username) > 20:
        return SignupResponse(
            status=False,
            message="Username length must be below 20"
        )
    
    # User not exist, create a new one
    cursor.execute("""
        INSERT INTO `users` 
            (`username`, `password`, `date_of_birth`, `email`)
        VALUES 
            (%(username)s, %(password)s, %(date_of_birth)s, %(email)s);
    """, body.model_dump())
    cursor.close()
    db.commit()

    return SignupResponse(
        status=True,
        message=""
    )