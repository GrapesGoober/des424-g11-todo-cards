
from fastapi import HTTPException, status
import jwt
import mysql.connector
from pydantic import BaseModel
from datetime import date, datetime, timedelta, timezone

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

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

class TokenPayload(BaseModel):
    username: str
    expire: datetime

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

def generate_token(body: LoginRequest) -> str:
    """
    Authenticates a user. 
    If success, would generate a JWT token.
    """
    conn = connect_to_db()
    cursor = conn.cursor()

    # Check Username Exists
    cursor.execute("""
        SELECT 
            `password`
        FROM 
            `users` 
        WHERE 
            `username` = %(username)s;
    """, body.model_dump())

    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is None:
        return "Username not found"
    
    password, = row
    if body.password != password:
        return "Password incorrect"

    payload = TokenPayload(
        username=body.username,
        expire=datetime.now(timezone.utc) + timedelta(minutes=1)
    )

    encoded_jwt = jwt.encode(payload.model_dump(mode='json'), SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt_username(token: str) -> str:
    """
    Verify that the authenticated token corresponds to a valid user and not expires.
    If token valids, returns username.
    """

    try:
        token_payload = TokenPayload(
            **jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWT Invalid"
        )
    
    # Verify expiration
    if datetime.now(timezone.utc) > token_payload.expire:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWT Expires"
        )
    
    conn = connect_to_db()
    cursor = conn.cursor()

    # Verify Username
    cursor.execute("""
        SELECT 
            1 
        FROM 
            `users` 
        WHERE 
            `username` = %(username)s;
    """, token_payload.model_dump())


    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWT Expires"
        )
    
    # Checks passed, returns username
    return token_payload.username