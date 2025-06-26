import requests

class PetAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def post_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.post(url, headers=self.headers, json=pet_data)
        return response
