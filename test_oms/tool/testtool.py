from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

#定义菜单切换，再切换表单函数
def switchPage(driver, menuName, childMenuName):
    driver.find_element_by_name(menuName).click()
    driver.find_element_by_link_text(childMenuName).click()
    # 切换表单
    driver.switch_to.frame("iframeBox")

#定义查询类
class query:
    #定义人员查询方法
    def queryUsers(self, driver, department, depValue, workNo, workName, linkText):
        self.driver = driver
        self.department = department
        self.depValue = depValue
        self.workNo = workNo
        self.workName = workName
        self.linkText = linkText
        #选择部门
        sel = self.driver.find_element_by_id(self.department)
        Select(sel).select_by_value(self.depValue)
        #输入人员姓名
        self.driver.find_element_by_id(self.workNo).send_keys(self.workName)
        time.sleep(1)
        #点击查询
        self.driver.find_element_by_link_text(self.linkText).click()

    #定义重置查询框方法
    def resetting(self, driver, linkText2, linkText):
        #点击重置
        driver.find_element_by_link_text(linkText2).click()
        #点击查询
        driver.find_element_by_link_text(linkText).click()

#定义新增类
class add:
    # 定义新增人员方法,linkTextAdd 新增按钮，linkTextSure 确定按钮
    def addUser(self, driver, linkTextAdd, userId, userIdValue, userName, userNameValue, sexValue, department, depNum, userRole, roleNum, telId, telNum, linkTextSure):
        self.linkTextAdd = linkTextAdd
        self.userId = userId
        self.userIdValue = userIdValue
        self.userName = userName
        self.userNameValue = userNameValue
        self.sexValue = sexValue
        self.department = department
        self.depNum = depNum
        self.userRole = userRole
        self.roleNum = roleNum
        self.telId = telId
        self.telNum = telNum
        self.linkTextSure = linkTextSure
        driver.find_element_by_link_text( self.linkTextAdd).click()
        driver.find_element_by_id(self.userId).send_keys(self.userIdValue)
        driver.find_element_by_id(self.userName).send_keys(self.userNameValue)
        driver.find_element_by_css_selector(self.sexValue).click()
        sel1 = driver.find_element_by_id(self.department)
        Select(sel1).select_by_value(self.depNum)
        role = driver.find_element_by_id(self.userRole)
        Select(role).select_by_value(self.roleNum)
        driver.find_element_by_id(self.telId).send_keys(self.telNum)
        driver.find_element_by_link_text(self.linkTextSure).click()
        time.sleep(2)

        # 接受新增人员成功提示框
        driver.switch_to.alert.accept()
