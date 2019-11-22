from selenium import webdriver
import time
from tool import logintool, testtool

#打开浏览器，设置隐式等待
driver = webdriver.Chrome()
driver.implicitly_wait(10)

#调用openBrowser方法访问测试地址
url = "http://10.238.2.63:9001/"
logintool.login().getUrl(driver, url)
#调用getCode方法获取验证码
region = (1190, 330, 1310, 375)
vcode = logintool.login().getCode(driver, region)
#调用login方法登录
logintool.login().start(driver, region, "userName", "admin", "password", "yzhxcql", "code", vcode, "loginBtn")

#进入账户管理-人员管理页面
time.sleep(1)
testtool.switchPage(driver, "02", "人员管理")
#测试查询人员功能
testtool.query().queryUsers(driver, "department", "0011", "workNo", "来顺", "查询")

#测试重置功能
testtool.query().resetting(driver, "重置", "查询")

#测试新增人员功能
testtool.add().addUser(driver, "新增人员", "userId", "19051018", "userName", "段誉", "input[value='2']", "department1", "0011", "role", "0001", "tel", "13352948334", "确定")



