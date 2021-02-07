import requests
from api.addCartApi import addCartApi
from api.loginApi import MtxLogin
from api.orderApi import Order


class TestOrder:
    def setup(self):
        self.session = requests.Session()
        self.order_obj = Order()

    def test_order(self):
        MtxLogin().login(self.session)
        addCartApi().add_cart(self.session)
        resp_order = self.order_obj.order(self.session)
        # print(resp_order.json())
        assert resp_order.status_code == 200
        # assert resp_order.json().get('msg') == '提交成功'



