from fastapi.testclient import TestClient

from config import settings


def test_health_check(client: TestClient) -> None:
    """Test health-check endpoint"""
    # Make request
    response = client.get(f"{settings.API_V1_STR}/utils/health-check/")

    # Assert response
    assert response.status_code == 200
    assert response.content
