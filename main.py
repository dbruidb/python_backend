
from fastapi import FastAPI
import uvicorn
import psycopg2
import os



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")

app = FastAPI()


host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")


connection_string= f"host={host} port={port} user={username} password={password} dbname={database}" # type: ignore
conn = psycopg2.connect(connection_string)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/resultados")
def resultados():
    return consultarDB("SELECT * FROM view_players_with_score")


def consultarDB(sql_sentence):
    cur = conn.cursor()
    cur.execute(sql_sentence)
    return cur.fetchall()

