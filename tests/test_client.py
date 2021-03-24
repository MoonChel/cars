import pytest

from cars.data_models import CarModel, CreateCarRequest
from cars.client.cars_client import CarsClient
from cars.client.base_client import ClientConfig

pytestmark = [pytest.mark.asyncio]


@pytest.fixture
async def test_api_client():
    client = CarsClient(
        ClientConfig(
            user_agent="Test",
            base_url="http://127.0.0.1:8000/api",
        ),
    )

    yield client

    await client.close_session()


@pytest.mark.vcr()
async def test_client_create_car(test_api_client: CarsClient):
    create_car_request = CreateCarRequest(
        name="Test",
        car_type="Test",
        year=2000,
    )

    new_car = await test_api_client.create_car(create_car_request)

    assert new_car.car_type == create_car_request.car_type
