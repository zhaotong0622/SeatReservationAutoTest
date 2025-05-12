import time

import minium
from minium import Callback

# 测试：命令行输入 minitest -m seat_reservation_auto_test -c config.json -g

# 查看报告： python -m http.server 12345 -d outputs
# 打开浏览器，访问http：//localhost:12345即可查看报告

# 测试用例必须以test_开头


class SeatReservationAutoTest(minium.MiniTest):
    # 测试用例1
    def test_get_system_info(self):
        sys_info = self.mini.get_system_info()
        self.assertIn("SDKVersion", sys_info)

    # 测试用例：学生登录_登录成功
    def test_login_success(self):
        page = self.page

        # 输入账号
        el = page.get_element("input[class='input'][placeholder='请输入账号']")
        el.input("123")
        time.sleep(3)

        # 输入密码
        el = page.get_element("input[class='input'][placeholder='请输入密码']")
        el.input("123")
        time.sleep(3)

        # 点击"立即登录"
        el = page.get_element("button[class='login-btn']", text_contains="立即登陆")
        el.click()

        # 查看是否登录成功
        page = self.page
        self.assertTrue(page.element_is_exists("view[class='submit-btn']", text_contains="提交申请"))
        # self.assertTrue()

    # 测试用例：学生登录_登录失败_账户不存在
    def test_login_failure_id(self):
        page = self.page

        # 输入账号
        el = page.get_element("input[class='input'][placeholder='请输入账号']")
        el.input("1234")
        time.sleep(3)

        # 输入密码
        el = page.get_element("input[class='input'][placeholder='请输入密码']")
        el.input("123")
        time.sleep(3)

        # 点击"立即登录"
        el = page.get_element("button[class='login-btn']", text_contains="立即登陆")
        el.click()

        # 查看是否登录成功
        page = self.page
        self.assertFalse(page.element_is_exists("view[class='submit-btn']", text_contains="提交申请"))
        # self.assertTrue()

    # 测试用例：学生登录_登录失败_密码错误
    def test_login_failure_key(self):
        page = self.page

        # 输入账号
        el = page.get_element("input[class='input'][placeholder='请输入账号']")
        el.input("123")
        time.sleep(3)

        # 输入密码
        el = page.get_element("input[class='input'][placeholder='请输入密码']")
        el.input("1234")
        time.sleep(3)

        # 点击"立即登录"
        el = page.get_element("button[class='login-btn']", text_contains="立即登陆")
        el.click()

        # 查看是否登录成功
        page = self.page
        self.assertFalse(page.element_is_exists("view[class='submit-btn']", text_contains="提交申请"))
        # self.assertTrue()


