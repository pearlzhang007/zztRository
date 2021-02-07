import requests

import api
import setting


class TestDelivery:
    def setup(self):
        self.session = requests.Session()
        self.payorder_obj = api.PayOrder()
        self.adminlogin_obj = api.AdminLogin()
        self.mtxlogin_obj = api.MtxLogin()
        self.addcart_obj = api.addCartApi()
        self.order_obj = api.Order()
        self.delivery_obj = api.Delivery()

    def teardown(self):
        self.session.close()

    def test_delivery(self):
        self.mtxlogin_obj.login(self.session)
        self.addcart_obj.add_cart(self.session)
        self.order_obj.order(self.session)
        self.adminlogin_obj.admin_login(self.session)
        print(self.payorder_obj.pay_order(self.session, setting.ORDER_ID, setting.PAYMENT_ID).json())
        resp_delivery = self.delivery_obj.delivery(self.session,setting.ORDER_ID,setting.USER_ID)
        print(resp_delivery.json())
        assert resp_delivery.status_code == 200
        # assert resp_delivery.json().get('msg') == '发货成功'

# pytest -s --alluredir ./reports/Raw/
# allure generate ./reports/Raw/ -o ./reports/html/ --clean