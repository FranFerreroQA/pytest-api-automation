import pytest
import logging

def pytest_configure(config):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@pytest.fixture
def base_url():
    return "https://petstore3.swagger.io/api/v3"

@pytest.fixture
def auth_headers():
    return {
        "Authorization": "Bearer xxx",
        "Content-Type": "application/json"
    }
