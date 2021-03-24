import enum
from .base_client import BaseClient
from cars.data_models import CreateCarRequest, CarModel


class CarsEndpoint(enum.Enum):
    CARS = "/cars"


class CarsClient(BaseClient):
    async def create_car(self, create_car_request: CreateCarRequest) -> CarModel:
        response = await self._session.post(
            self._url_for(CarsEndpoint.CARS), json=create_car_request.dict()
        )

        json = response.json()

        return CarModel(**json)
