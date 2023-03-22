import requests


def get_all_books(type = '', limit = ''):
    if type == '' and limit == '':
        make_request = requests.get('https://simple-books-api.glitch.me/books')
    elif type != '' and limit == '':
        make_request = requests.get(f'https://simple-books-api.glitch.me/books?type={type}')
    elif type == '' and limit != '':
        make_request = requests.get(f'https://simple-books-api.glitch.me/books?limit={limit}')
    else:
        make_request = requests.get(f'https://simple-books-api.glitch.me/books?type={type}&limit={limit}')

    return make_request
