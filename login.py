import pytest


class TestLogin:

    def setup(self):
        print("setup")
        print("打开商城")

    def teardown(self):
        print("teardown")
        print("关闭商城")

    def test_login_01(self):
        print("首页，查询商品")
        print("添加购物车")
        print("支付")

    def test_login_02(self):
        print("添加购物车")

    @pytest.mark.run(order=1)
    def test_login_03(self):
        print("支付")
