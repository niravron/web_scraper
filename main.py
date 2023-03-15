import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/wikipedia/personal-info")



