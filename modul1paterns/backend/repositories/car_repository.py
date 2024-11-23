from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from database import Database
from models.car import Car
from schemas.car_schema import CarCreate, CarUpdate


class CarRepository:
    def __init__(self):
        self.db: AsyncSession = Database().get_session()

    async def create_car(self, car: Car):
        async with self.db as session:
            async with session.begin():
                session.add(car)
                await session.flush()
                await session.refresh(car)
                return car

    async def get_cars(self):
        async with self.db as session:
            query = select(Car)
            result = await session.execute(query)
            return result.scalars().all()

    async def get_car(self, car_id: UUID):
        async with self.db as session:
            query = select(Car).where(Car.id == car_id)
            result = await session.execute(query)
            car = result.scalar_one_or_none()
            if not car:
                raise NoResultFound
            return car

    async def update_car(self, car_id: UUID, car_data: CarUpdate):
        async with self.db as session:
            query = select(Car).where(Car.id == car_id)
            result = await session.execute(query)
            car = result.scalar_one_or_none()
            if not car:
                raise NoResultFound

            # Оновлення даних автомобіля
            if car_data.model:
                car.model = car_data.model
            if car_data.manufacturer:
                car.manufacturer = car_data.manufacturer
            if car_data.description:
                car.description = car_data.description
            if car_data.year:
                car.year = car_data.year

            await session.commit()
            await session.refresh(car)
            return car

    async def delete_car(self, car_id: UUID):
        async with self.db as session:
            query = select(Car).where(Car.id == car_id)
            result = await session.execute(query)
            car = result.scalar_one_or_none()
            if not car:
                raise NoResultFound

            await session.delete(car)
            await session.commit()
