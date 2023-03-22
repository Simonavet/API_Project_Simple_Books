from requests_folder.get_all_books import *

class TestAllBooks:
    def test_get_all_books_no_filter_no_type_status_code(self):
        make_request = get_all_books('','')
        assert make_request.status_code == 200, f'Error: Wrong status code. Expected:200, Actual: {make_request.status_code}'

    def test_get_all_books_no_filter_no_type_nr_rez(self):
        make_request = get_all_books()
        assert len(make_request.json())== 6, f"Expected: 6, actual: {len(make_request.json())}"

    def test_get_all_books_type_fiction(self):
        make_request = get_all_books('fiction', '').json()
        assert len(make_request) == 4, f'Expected:4, actual: {len(make_request)}'
        for i in range(len(make_request)):
            assert make_request[i]['type'] == 'fiction', f"Error: Book {make_request[i]['name']} has an invalid type."

    def test_get_all_books_type_non_fiction(self):
        make_request = get_all_books('non-fiction', '').json()
        assert len(make_request) == 2, f'Expected:2, actual: {len(make_request)}'
        for i in range(len(make_request)):
            assert make_request[i]['type'] == 'non-fiction', f"Error: Book {make_request[i]['name']} has an invalid type."

    def test_get_all_books_type_invalid(self):
        make_request = get_all_books('adventure', '')
        assert make_request.status_code == 400
        assert make_request.json()["error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", 'Error is not correct!'

    def test_get_all_books_limit_invalid(self):
        make_request = get_all_books('', '21')
        assert make_request.status_code == 400
        assert make_request.json()["error"] == "Invalid value for query parameter 'limit'. Cannot be greater than 20.", "Error is not correct!"

    def test_get_all_books_type_fiction_limit_2(self):
        make_request = get_all_books('fiction', 2)
        assert make_request.status_code == 200

    def test_get_all_books_type_non_fiction_limit_1(self):
        make_request = get_all_books('non-fiction', 1)
        assert make_request.status_code == 200

    def test_get_all_books_no_type_limit_3(self):
        make_request = get_all_books('', 3)
        assert make_request.status_code == 200

    def test_get_all_books_no_type_limit_0(self):
        make_request = get_all_books('', 0)
        assert make_request.status_code == 200

    def test_get_all_books_no_type_limit_1(self):
        make_request = get_all_books('', 1)
        assert make_request.status_code == 200

    def test_get_all_books_no_type_limit_20(self):
        make_request = get_all_books('', 20)
        assert make_request.status_code == 200

    def test_get_all_books_no_type_limit_7(self):
        make_request = get_all_books('', -7)
        assert make_request.status_code == 400
        assert make_request.json()["error"] == "Invalid value for query parameter 'limit'. Must be greater than 0.", "Error is not correct!"
