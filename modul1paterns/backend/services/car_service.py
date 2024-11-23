from repositories.car_repository import CarRepository
from schemas.car_schema import CarCreate, CarUpdate
from uuid import UUID
from models.car import Car

class CarService:
    def __init__(self):
        self.repository = CarRepository()

    async def add_car(self, car: Car):
        return await self.repository.create_car(car)

    async def list_cars(self):
        return await self.repository.get_cars()

    async def get_car(self, car_id: UUID):
        return await self.repository.get_car(car_id)

    async def update_car(self, car_id: UUID, car_data: CarUpdate):
        return await self.repository.update_car(car_id, car_data)

    async def delete_car(self, car_id: UUID):
        return await self.repository.delete_car(car_id)
