import psycopg2
import traceback

from config import host, user, password, port, db_name

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
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

