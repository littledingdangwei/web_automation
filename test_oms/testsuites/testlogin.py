import unittest
from logmaker.logger import Logger
from framework.browser_engine import BrowserEngine
from tool import logintool
from time import sleep

logger = Logger(logger='testLogin').getLog()

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserEngine()
        cls.driver = cls.browser.open_browser()
        cls.login = logintool.login()

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.browser.quit_browser()
        sleep(1)
        # cls.driver.quit()
    #测试 访问测试服务器地址首页
    def test_shouYe(self):
        try:
            self.login.getUrl(self.driver,"http://10.238.2.63:9001/")
            loginBtn = self.driver.find_element_by_id('loginBtn').text
            self.assertEqual(self.driver.title,'登录')

        except Exception as e:
            logger.error("访问测试地址登录页失败：%s"%e)

        sleep(1)
    #测试 登录
    def test_login(self):
        try:
            region = (1190, 330, 1310, 375)
            vcode = self.login.getCode(self.driver,region)
            self.login.start(self.driver, 'admin', 'yzhxcql', vcode, region)
            self.assertEqual(self.driver.title,'主页')
        except Exception as e:
            print("登录失败,%s"%e)

if __name__ == '__main__':
    unittest.main()