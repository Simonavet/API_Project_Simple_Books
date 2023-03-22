from requests_folder.order_view import *
from requests_folder.order import submit_order


class TestGetOrder:
    def test_get_order_status_code(self):
        make_request = get_order()
        assert make_request.status_code == 200, f'Error: Wrong status code Expected:200, Actual: {make_request.status_code}'

    def test_get_order_by_id(self):
        order_id = submit_order(1, 'John').json()['orderId']
        make_request = get_order(order_id)
        assert make_request.status_code == 200, f'Error: Wrong status code Expected:200, Actual: {make_request.status_code}'
