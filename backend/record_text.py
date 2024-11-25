import mysql.connector
from pydantic import BaseModel

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

class RecordTextBody(BaseModel):
    text: str

def record(body: RecordTextBody):
    db = connect_to_db()
    cursor = db.cursor()

    # Insert the text into the table
    cursor.execute("INSERT INTO `text_records` (text) VALUES (%(text)s)", body.model_dump())

    cursor.close()
    db.commit()

    return True