from fastapi import APIRouter, Response

from cars.db.models import Car
from cars.common.data_models import CreateCarRequest, CarModel

router = APIRouter(prefix="/api")


@router.post("/ping")
async def ping():
    return Response("pong")


@router.post("/cars", response_model=CarModel)
async def create_car(car_request: CreateCarRequest):
    car_request_dict = car_request.dict()

    car = await Car.create(**car_request_dict)

    return CarModel.from_orm(car)
