from fastapi import FastAPI, HTTPException, Body
from datetime import date
from pymongo import MongoClient
from pydantic import BaseModel

DATABASE_NAME = "exceed07"
COLLECTION_NAME = "locker"
MONGO_DB_URL = "mongodb://exceed07:8td6VF6w@mongo.exceed19.online:8443/?authMechanism=DEFAULT"
MONGO_DB_PORT = 8443


class Locker(BaseModel):
    locker_id : int
    student_id: str
    duration: int
    items: list




client = MongoClient(f"{MONGO_DB_URL}:{MONGO_DB_PORT}")

db = client[DATABASE_NAME]

collection = db[COLLECTION_NAME]

app = FastAPI()


@app.get("/locker/{locker_id}/{student_id}/{duration}/{items}")
def show_locker(locker_id: int, student_id: str, duration: int, items: list):
    return {"locker_id": locker_id, "student_id": student_id, "duration": duration, "items": items}

#query
@app.get("/locker")
def query_item(locker_id: int, student_id: str, duration: int, items: list):
    return {"locker_id": locker_id, "student_id": student_id, "duration": duration, "items": items}

@app.get("/locker/body")
def with_body(locker_id: int = Body(), student_id: str = Body(), duration: int = Body(), items: list = Body()):
    return {"locker_id": locker_id, "student_id": student_id, "duration": duration, "items": items}

# #BaseModel
# @app.get("/items/with_body_with_params")
# def show_item_body_with_query(item: Item, item_color: str = Body()):
#     new_item_id = "s" + str(item.item_id)
#     return {"item": item, "item_color": item_color}

# @app.get("/reservation/by-name/{name}")
# def get_reservation_by_name(name:str):
#     hotel = []
#     for i in collection.find({"name": name}, {"_id":False}):
#         hotel.append(i)
#     return {"result": hotel}


# @app.get("/reservation/by-room/{room_id}")
# def get_reservation_by_room(room_id: int):
#     hotel = []
#     for i in collection.find({"room_id": room_id}, {"_id":False}):
#         hotel.append(i)
#     return {"result": hotel}

# @app.post("/reservation")
# def reserve(reservation : Reservation):
#     if not room_avaliable:
#         raise HTTPException(status_code=400)
#     if reservation.start_date > reservation.end_date:
#         raise HTTPException(status_code=400)
#     if reservation.room_id not in range(1,11):
#         raise HTTPException(status_code=400)
#     collection.insert_one({
#         "name": reservation.name, 
#         "start_date": str(reservation.start_date), 
#         "end_date": str(reservation.end_date), 
#         "room_id": reservation.room_id
#         })

# @app.put("/reservation/update")
# def update_reservation(reservation: Reservation, new_start_date: date = Body(), new_end_date: date = Body()):
#     if not room_avaliable:
#         raise HTTPException(status_code=400)
#     if reservation.start_date > reservation.end_date:
#         raise HTTPException(status_code=400)
#     if reservation.room_id not in range(1,11):
#         raise HTTPException(status_code=400)
#     collection.update_one({
#         "name": reservation.name, 
#         "room_id": reservation.room_id}, 
#         {"$set": {
#             "start_date": str(new_start_date), 
#             "end_date": str(new_end_date)
#             }
#         }, upsert=True)

# @app.delete("/reservation/delete")
# def cancel_reservation(reservation: Reservation):
#     collection.delete_one({
#         "name": reservation.name, 
#         "start_date": str(reservation.start_date), 
#         "end_date": str(reservation.end_date), 
#         "room_id": reservation.room_id
#         })
