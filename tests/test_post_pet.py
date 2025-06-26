from pages.pet_api import PetAPI
import random
import logging

logger = logging.getLogger(__name__)

# Happy path: postear nueva mascota
def test_post_pet(base_url, auth_headers):
    api = PetAPI(base_url, auth_headers)

    random_id = random.randint(1, 999)

    pet_data = {
        "id": random_id,
        "name": "Challenge",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "https://media.istockphoto.com/id/115683561/es/foto/jack-russell-terrier-diez-meses-de-edad-sentado-fondo-blanco.webp?s=2048x2048&w=is&k=20&c=liQxjp5oI477Wmz0qcc1ESj5D6YPcd6EB4ky9aHxOEg="
        ],
        "tags": [
            {
                "id": random_id,
                "name": "Challenge"
            }
        ],
        "status": "available"
    }

    response = api.post_pet(pet_data)

    # Assertions
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    response_time = response.elapsed.total_seconds()
    assert response_time < 1, f"Expected response time < 1 second, got {response_time:.2f} seconds"
    
    assert response.json().get("status") == "available", f"Expected status 'available', got {response.json().get('status')}"

    # Logging
    logger.info(f"Tested with pet ID: {random_id}")
    logger.info(f"Status: {response.json().get('status')}")
    logger.info(f"Response time: {response_time:.2f} seconds")

# Negative test: postear mascota con id vacio
def test_empty_id_pet(base_url, auth_headers):
    api = PetAPI(base_url, auth_headers)
    
    pet_data = {
        "id": None,  # Intentionally set to None to test empty ID
        "name": "Challenge",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "https://media.istockphoto.com/id/115683561/es/foto/jack-russell-terrier-diez-meses-de-edad-sentado-fondo-blanco.webp?s=2048x2048&w=is&k=20&c=liQxjp5oI477Wmz0qcc1ESj5D6YPcd6EB4ky9aHxOEg="
        ],
        "tags": [
            {
        "id": 123,
        "name": "Challenge"
        }
    ],
    "status": "available"
    }
    
    response = api.post_pet(pet_data)

    # Assertions
    assert response.status_code == 500, f"Expected 500, got {response.status_code}"

    assert "error processing your request" in response.json().get("message"), f"Expected partial message, got {response.json().get('message')}"

    response_time = response.elapsed.total_seconds()
    assert response_time < 1, f"Expected response time < 1 second, got {response_time:.2f} seconds"

    # Logging
    logger.warning(f"Received error response: {response.json()}")
    logger.info(f"Response time: {response_time:.2f} seconds")