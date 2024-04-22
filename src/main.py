import psycopg2
import traceback

import uvicorn
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from models.roles_permissions import Roles
from models.db_config import host, user, password, db_name, port

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def has_permission():
    pass


@app.get("/protected_resource")
async def protected_resource():
    return {"message": "This is a protected resource"}


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM "DBSchema".users;"""
        )

        print(f"Query result: {cursor.fetchone()}")

except Exception as _ex:
    print(_ex)
    traceback.print_exc()
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")


if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8000)
