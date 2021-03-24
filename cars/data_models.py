from pydantic import BaseModel


class CarBase(BaseModel):
    name: str
    car_type: str
    year: int


class CreateCarRequest(CarBase):
    pass


class CarModel(CarBase):
    id: int

    class Config:
        orm_mode = True
