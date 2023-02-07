from fastapi import FastAPI, HTTPException, Body
from datetime import date,datetime
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Union


DATABASE_NAME = "exceed07"
COLLECTION_NAME = "locker_man"
MONGO_DB_URL = f"mongodb://exceed07:8td6VF6w@mongo.exceed19.online"   # mongodb://localhost
MONGO_DB_PORT = 8443

client = MongoClient(f"{MONGO_DB_URL}:{MONGO_DB_PORT}/?authMechanism=DEFAULT")

db = client[DATABASE_NAME]

collection = db[COLLECTION_NAME]

app = FastAPI()

class locker(BaseModel):
    locker_id : int
    user_id : Union[str,None]
    available : bool
    start_time : datetime
    expected_stop_time : datetime
    content : Union[str,None]




#@app


#@app


#@app