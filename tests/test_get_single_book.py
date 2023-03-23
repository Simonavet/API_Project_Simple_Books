from requests_folder.get_single_book import *

class TestSingleBook:
    def test_get_single_book_identification_3(self):
        make_request = get_single_book(3)
        assert make_request.status_code == 200, f'Error: Wrong status code. Expected:200, Actual: {make_request.status_code}'

    def test_get_single_book_identification_6(self):
        make_request = get_single_book(6)
        assert make_request.status_code == 200, f'Error: Wrong status code. Expected:200, Actual: {make_request.status_code}'