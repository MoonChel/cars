import pytest
from httpx import AsyncClient

from cars.api.app import app
from cars.db.models import db
from cars.common.data_models import CreateCarRequest
from cars.api.settings import DB_URL

pytestmark = [pytest.mark.asyncio]


@pytest.fixture(autouse=True)
async def db_bind():
    await db.set_bind(DB_URL)
    await db.gino.create_all()
    print("DB started")

    yield

    print("DB exit")
    await db.gino.drop_all()
    await db.pop_bind().close()


@pytest.fixture
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


async def test_ping(test_client: AsyncClient):
    response = await test_client.post("/api/ping")

    assert response.status_code == 200
    assert response.text == "pong"


async def test_app(test_client: AsyncClient):
    create_car_request = CreateCarRequest(
        name="Test",
        car_type="Test Type",
        year=2000,
    )

    response = await test_client.post("/api/cars", json=create_car_request.dict())

    assert response.status_code == 200
