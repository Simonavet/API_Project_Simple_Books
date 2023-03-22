import requests


def get_single_book(identification = ''):
    make_request = requests.get(f'https://simple-books-api.glitch.me/books/{identification}')
    return make_request
