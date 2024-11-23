from uuid import uuid4
from models.car import Car

class CarBuilder:
    def __init__(self):
        self._id = None
        self._model = None
        self._manufacturer = None
        self._description = None
        self._year = None

    def set_model(self, model: str):
        self._model = model
        return self

    def set_manufacturer(self, manufacturer: str):
        self._manufacturer = manufacturer
        return self

    def set_description(self, description: str):
        self._description = description
        return self

    def set_year(self, year: int):
        self._year = year
        return self

    def build(self) -> Car:
        return Car(
            id=uuid4(),
            model=self._model,
            manufacturer=self._manufacturer,
            description=self._description,
            year=self._year
        )
