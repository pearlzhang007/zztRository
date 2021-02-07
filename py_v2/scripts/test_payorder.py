import requests
import api
import setting


class TestPayOrder:
    def setup(self):
        self.session = requests.Session()
        self.payorder_obj = api.PayOrder()
        self.adminlogin_obj = api.AdminLogin()
        self.mtxlogin_obj = api.MtxLogin()
        self.addcart_obj = api.addCartApi()
        self.order_obj = api.Order()

    def test_payorder(self):
        self.mtxlogin_obj.login(self.session)
        self.addcart_obj.add_cart(self.session)
        self.order_obj.order(self.session)
        self.adminlogin_obj.admin_login(self.session)
        resp_payorder = self.payorder_obj.pay_order(self.session, setting.ORDER_ID, setting.PAYMENT_ID)
        assert resp_payorder.status_code == 200
        # assert resp_payorder.json().get('msg')=='支付成功'
