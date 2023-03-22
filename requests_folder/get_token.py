import random
import requests


def generate_token():
    nr = random.randint(1, 9999999999999999999999999999999999)
    request_body = {
        "clientName": f"Postman{nr}",
        "clientEmail": f"jessy{nr}@example.com"
    }
    make_request = requests.post('https://simple-books-api.glitch.me/api-clients/', json=request_body)
    token = make_request.json()['accessToken']

    return token

