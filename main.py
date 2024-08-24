from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware

from db import Database
from depends import get_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    return "pong"
