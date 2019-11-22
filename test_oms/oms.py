from selenium import webdriver
import time
from PIL import Image
import pytesseract
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

#定义获得验证码字符串方法
def getCode():
    #窗口全屏截图
    driver.save_screenshot("1.png")
    #打开刚刚截取的窗口截图
    img = Image.open("1.png")
    #用左上角和右下角坐标锁定验证码图片
    region = (1190, 330, 1310, 375)
    #从整个窗口截图中，截取验证码图片
    nimg = img.crop(region)
    nimg.save("2.png")
    #打开验证码截图
    img2 = Image.open("2.png")
    vcode = pytesseract.image_to_string(img2)
    return vcode

#定义登录方法
def login(vcode):
    # 输入用户名、密码、验证码、点击提交
    driver.find_element_by_id("userName").send_keys("admin")
    driver.find_element_by_id("password").send_keys("yzhxcql")
    driver.find_element_by_id("code").send_keys(vcode)
    driver.find_element_by_id("loginBtn").click()

#打开浏览器，访问测试地址
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://10.238.2.63:9001/")
#最大化浏览器窗口
driver.maximize_window()
time.sleep(1)
#调用getCode方法并登录
vcode = getCode()
login(vcode)
#延迟1秒，判断是否有弹框弹出
time.sleep(1)
result = EC.alert_is_present()(driver)
#如果有弹框，则重新登录，直到成功
while result:
    print(result.text)
    result.accept()
    time.sleep(1)
    driver.find_element_by_id("userName").clear()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("code").clear()
    driver.find_element_by_class_name("code").click()
    vcode = getCode()
    login(vcode)
    time.sleep(1)

#定义菜单切换，再切换表单方法
def switchPage(menuName,childMenuName):
    driver.find_element_by_name(menuName).click()
    driver.find_element_by_link_text(childMenuName).click()
    # 切换表单
    driver.switch_to.frame("iframeBox")

#进入账户管理-人员管理页面
time.sleep(1)
switchPage("02","人员管理")

#测试查询功能
sel = driver.find_element_by_name("orderType")
Select(sel).select_by_value("0011")
driver.find_element_by_id("workNo").send_keys("来顺")
time.sleep(1)
driver.find_element_by_link_text("查询").click()
#测试重置功能
driver.find_element_by_link_text("重置").click()
driver.find_element_by_link_text("查询").click()
#测试新增人员功能
driver.find_element_by_link_text("新增人员").click()
driver.find_element_by_id("userId").send_keys("19080063")
driver.find_element_by_id("userName").send_keys("侯江涛")
driver.find_element_by_css_selector("input[value='2']").click()
sel1 = driver.find_element_by_id("department1")
Select(sel1).select_by_value("0011")
role = driver.find_element_by_id("role")
Select(role).select_by_value("0001")
driver.find_element_by_id(("tel")).send_keys("13352948334")
driver.find_element_by_link_text("确定").click()
time.sleep(2)

#接受新增人员成功提示框
driver.switch_to.alert.accept()
