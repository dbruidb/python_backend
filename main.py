
from fastapi import FastAPI
import uvicorn
import psycopg2
import os
from psycopg2.extras import RealDictCursor
import asyncpg

from  routes import general



#la app a ser emitida
app = FastAPI()

#Rutas hijas

app.include_router(general.router)

#Rutas

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/resultados")
def resultados():
    return consultarDB("SELECT * FROM view_results_with_names")

@app.get("/res")
async def res():
    return await consultarAsyncDB("SELECT * FROM view_results_with_names")


#Conexion Database

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")


connection_string= f"host={host} port={port} user={username} password={password} dbname={database}" # type: ignore
conn = psycopg2.connect(connection_string)

async def connect():
    aconn = await asyncpg.connect(user = username, password = password, database = database, host = host, port = port)
    return aconn



#Database Defs

def consultarDB(sql_sentence):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql_sentence)
    return cur.fetchall()

async def consultarAsyncDB(sql_sentence):
    await connect().fetch(sql_sentence)

