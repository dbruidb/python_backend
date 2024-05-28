
from fastapi import FastAPI
import uvicorn
import psycopg2


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")

app = FastAPI()


connection_string= f"host={process.env.DB_HOST} port={process.env.DB_PORT} user={process.env.DB_USERNAME} password={process.env.DB_PASSWORD} dbname={process.env.DB_DATABASE}" # type: ignore
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

