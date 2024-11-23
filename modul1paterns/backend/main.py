from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import NoResultFound
from uuid import UUID

from builders.car_builder import CarBuilder
from services.car_service import CarService
from schemas.car_schema import CarCreate, CarRead, CarUpdate

app = FastAPI()
car_service = CarService()

app.add_middleware(
    CORSMiddleware,
    allow_origins='http://127.0.0.1:5500',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/car/", response_model=CarRead)
async def create_car(car_data: CarCreate):
    builder = CarBuilder()
    car = builder \
        .set_model(car_data.model) \
        .set_manufacturer(car_data.manufacturer) \
        .set_description(car_data.description) \
        .set_year(car_data.year) \
        .build()

    return await car_service.add_car(car)

@app.get("/api/car/", response_model=list[CarRead])
async def read_cars():
    return await car_service.list_cars()

@app.get("/api/car/{car_id}", response_model=CarRead)
async def read_car(car_id: UUID):
    try:
        return await car_service.get_car(car_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Car not found")

@app.put("/api/car/{car_id}", response_model=CarUpdate)
async def update_car(car_id: UUID, car: CarUpdate):
    try:
        return await car_service.update_car(car_id, car)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Car not found")

@app.delete("/api/car/{car_id}", response_model=dict)
async def delete_car(car_id: UUID):
    try:
        await car_service.delete_car(car_id)
        return {"detail": "Car deleted"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Car not found")
