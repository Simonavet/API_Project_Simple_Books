from requests_folder.order import submit_order
from requests_folder.update_order import *


class TestUpdateOrder:
    def test_update_order(self):
        order_id = submit_order(1, 'John').json()['orderId']
        make_request = update_order('Simona', order_id)
        assert make_request.status_code == 204, f'Error: Wrong status code Expected:204, Actual: {make_request.status_code}'