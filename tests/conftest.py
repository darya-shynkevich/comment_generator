from collections.abc import Generator

import pytest
from faker import Faker
from fastapi.testclient import TestClient

from config import settings
from main import app
from supabase import Client, create_client


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def super_client() -> Generator[Client, None]:
    super_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    yield super_client


fake = Faker()
