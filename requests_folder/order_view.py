import requests
from requests_folder.get_token import generate_token


def get_order(order_id=''):
    token = generate_token()
    header_params = {'Authorization': token}

    if order_id == '':
        make_request = requests.get('https://simple-books-api.glitch.me/orders', headers=header_params)
    else:
        make_request = requests.get(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=header_params)

    return make_request

