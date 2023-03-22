from requests_folder.order import submit_order
from requests_folder.vanish_order import delete_order


class TestDeleteOrder:
    def test_delete_order_valid_order_id(self):
        order_id = submit_order(1, 'Simona').json()['orderId']
        make_request = delete_order(order_id)
        assert make_request.status_code == 204, f"Error: Wrong status code. Expected:204, actual: {make_request.status_code}"

    def test_delete_order_invalid_id(self):
        make_request = delete_order('jdhfg4865eehfh')
        assert make_request.status_code == 404, f"Error: Wrong status code. Expected:401, actual: {make_request.status_code}"