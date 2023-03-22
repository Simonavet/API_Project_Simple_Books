import requests
from requests_folder.get_token import generate_token


def update_order(customer_name, order_id):
    request_body = {

            "customerName": customer_name
    }
    token = generate_token()
    header_params = {'Authorization': token}
    make_request = requests.patch(f'https://simple-books-api.glitch.me/orders/{order_id}', json=request_body, headers=header_params)

    return make_request
