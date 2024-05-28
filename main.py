
from fastapi import FastAPI
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
