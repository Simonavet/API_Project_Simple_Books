from requests_folder.order import submit_order


class TestOrder:
    def test_submit_order(self):
        make_request = submit_order(1, 'John')
        assert make_request.status_code == 201, f"Error: Wrong status code. Expected:201, actual: {make_request.status_code}"
        assert make_request.json()["created"] == True, f"Error:Order not created. Expected: True, Actual: {make_request.json()['created']}"
        assert len(make_request.json()["orderId"]) > 0, f"Error:Invalid order. Expected lengh must > 0. Actual length: {len(make_request.json()['orderId'])}"

    def test_submit_order_invalid(self):
        make_request = submit_order(1003, 'John')
        assert make_request.status_code == 400

    def test_submit_order_invalid_error_msg(self):
        make_request = submit_order(1003, 'John')
        assert make_request.json()['error'] == 'Invalid or missing bookId.'

