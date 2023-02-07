# from fastapi import FastAPI, HTTPException, Body
import datetime
# from pymongo import MongoClient
# from pydantic import BaseModel
# from typing import Union


# DATABASE_NAME = "exceed07"
# COLLECTION_NAME = "locker_man"
# MONGO_DB_URL = f"mongodb://exceed07:8td6VF6w@mongo.exceed19.online"   # mongodb://localhost
# MONGO_DB_PORT = 8443

# client = MongoClient(f"{MONGO_DB_URL}:{MONGO_DB_PORT}/?authMechanism=DEFAULT")

# db = client[DATABASE_NAME]

# collection = db[COLLECTION_NAME]

# app = FastAPI()

# class locker(BaseModel):
#     locker_id : int
#     user_id : Union[str,None]
#     available : bool
#     start_time : datetime.datetime
#     expected_stop_time : datetime.datetime
#     content : Union[str,None]


# def init():
#     for i in range(1, 7):
#         collection.insert_one({
#         "locker_id": i,
#         "user_id": None,
#         "available" : True,
#         "start_time": None,
#         "expected_stop_time": None,
#         "content": None
#     })

# @app.get("/find_available_locker")
# def find_available_locker():
#     available = []
#     for i in collection.find({}):
#         i = dict(i)
#         if i["available"]:
#             available.append(i["locker_id"])
#     return {"available_locker":available}


# @app.get("/locker_reserve")
# def query_item(locker_id: int, user_id: Union[str, None], duration: int, content: Union[str, None]):
#     locker = collection.find_one({"locker_id": locker_id})
#     locker = dict(locker)
#     start_time = datetime.datetime.now().total_minutes()
#     if not locker["available"]:
#         raise HTTPException(status_code=400)
#     ex = start_time + datetime.timedelta(minutes=duration)
#     start_time = start_time.strftime("%Y-%m-%d:%H-%M-%S")
#     ex = ex.strftime("%Y-%m-%d:%H-%M-%S")
#     collection.update_one({"locker_id": locker_id}, {"$set": {"user_id": user_id,"available": False, "start_time": str(start_time), "expected_stop_time": str(ex), "content": content}})

# #@app
print(datetime.datetime.now().total_seconds())