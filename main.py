from fastapi import FastAPI, HTTPException, Body
import datetime
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Union
import math


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
    start_time : datetime.datetime
    expected_stop_time : datetime.datetime
    content : Union[str,None]


#@app


#@app
    


@app.put("/locker_retrieve")
def query_item(locker_id: int, user_id : Union[str,None], out_time: str, money: float):
        x = collection.find_one({"user_id": user_id, "locker_id": locker_id, "available": False})
        if x is None:
            raise HTTPException(status_code=400, detail="NOT FOUND")

        x = dict(x)
        start_time = x["start_time"]
        expected_stop_time = x["expected_stop_time"]

        start = datetime.datetime.strptime(start_time, "%Y-%m-%d:%H-%M-%S")
        out = datetime.datetime.strptime(out_time, "%Y-%m-%d:%H-%M-%S")
        end = datetime.datetime.strptime(expected_stop_time, "%Y-%m-%d:%H-%M-%S")
        
        use_time = out - start
        overflow = out - end
        price = 0

        if overflow >= datetime.timedelta(minutes=0):
            price += 20*(math.ceil(overflow/datetime.timedelta(minutes=10)))
        
        if use_time > datetime.timedelta(hours=2):
            use_time -= datetime.timedelta(hours=2)
            price += 5*(math.ceil(use_time/datetime.timedelta(hours=1)))

        if money-price < 0:
            raise HTTPException(status_code=400, detail="TOO LITTLE MONEY")
        elif money-price > 0:
            collection.update_one({"locker_id": locker_id}, {"$set": {
                                                            "user_id": None,
                                                            "available" : True,
                                                            "start_time": None,
                                                            "expected_stop_time": None,
                                                            "content": None
                                                            }})
            return ({"msg": money-price})

        

    





