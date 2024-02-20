# fastapi_endpoints.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/process")
async def read_item():
    return {"message": "This is a FastAPI endpoint"}
