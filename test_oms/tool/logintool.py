from PIL import Image
import pytesseract
import time
from selenium.webdriver.support import expected_conditions as EC

class login:
    #定义打开谷歌浏览器,访问测试地址函数
    def getUrl(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)

    #定义获得验证码字符串函数 （lx,ly）是待锁定区域左上角坐标，（rx,ry）是右下角坐标
    def getCode(self, driver, region):
        self.driver = driver
        self.region = region
        # 最大化浏览器窗口
        self.driver.maximize_window()
        time.sleep(1)
        #窗口全屏截图
        self.driver.save_screenshot("1.png")
        #打开刚刚截取的窗口截图
        img = Image.open("1.png")
        #用左上角和右下角坐标锁定验证码图片
        self.region = region
        #从整个窗口截图中，截取验证码图片
        nimg = img.crop(region)
        nimg.save("2.png")
        #打开验证码截图
        img2 = Image.open("2.png")
        vcode = pytesseract.image_to_string(img2)
        return vcode

    #定义登录函数
    def start(self, driver, userName, password, vcode, region):
        self.driver = driver
        self.vcode = vcode
        self.userName = userName
        self.password = password
        self.region = region

        # 输入用户名、密码、验证码、点击提交
        self.driver.find_element_by_id('userName').send_keys(self.userName)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('code').send_keys(self.vcode)
        self.driver.find_element_by_id('loginBtn').click()
        # 延迟1秒，判断是否有弹框弹出
        time.sleep(1)
        result = EC.alert_is_present()(self.driver)
        # 如果有弹框，则重新登录，直到成功
        while result:
            time.sleep(1)
            result.accept()
            time.sleep(1)
            self.driver.find_element_by_id("userName").clear()
            self.driver.find_element_by_id("password").clear()
            self.driver.find_element_by_id("code").clear()
            self.driver.find_element_by_class_name("code").click()

            self.vcode = login().getCode(self.driver, self.region)
            print(self.vcode)
            login().start(self.driver, self.userName, self.password, self.vcode, self.region)
            time.sleep(1)
            result = EC.alert_is_present()(self.driver)