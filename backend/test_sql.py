# This script is EXPERIMENTAL
# This connects to mysql container as defined in compose.yaml
# SQL database defined as follows, for testing purposes.
# You can use fastapi docs to check this works
#   CREATE DATABASE records;
#   USE records;
#   CREATE TABLE records (
#       text TEXT
#   );
# Ideally, we'd refactor this to fit into the codebase a bit better
# Question: how can we design the software architecture? The coding part?
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

def connect_to_db():
    # these configs are defined in compose.yaml
    return mysql.connector.connect(
        host="mysql", # connects to mysql container, instead of normally via "localhost"
        user="root",
        password="12345678",
        database="records"
    )

class RecordTextBody(BaseModel):
    text: str

@app.post("/api/send_to_sql")
async def send_to_sql(body: RecordTextBody):
        
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO `records` (`text`) VALUES (%s)", (body.text,))
    mycursor.close()
    mydb.commit()

    return True