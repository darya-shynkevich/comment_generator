import logging

from fastapi.testclient import TestClient

from app.utils.test_pre_start import main as pre_start

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_pre_start() -> None:
    pre_start()


def test_root(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
