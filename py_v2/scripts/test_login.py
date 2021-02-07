import os, sys

from api import MtxLogin

sys.path.append(os.getcwd())

import pytest
import requests

# from api.loginApi import MtxLogin
class TestLogin:
    def setup(self):
        self.session = requests.Session()
        self.login_obj = MtxLogin()

    def test_login(self):
        resp_login = self.login_obj.login(self.session)
        # print(resp_login.json())
        assert resp_login.status_code == 200
        assert resp_login.json().get("msg") == '登录成功'


    def teardown(self):
        self.session.close()

if __name__ == '__main__':
    pytest.main()