# !/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from testsuites.testlogin import TestLogin
from testsuites.HTMLTestRunner import HTMLTestRunner
import os
import time

#添加用例到组件
testCases = [TestLogin("test_shouYe"),TestLogin("test_login")]
suite = unittest.TestSuite()
suite.addTests(testCases)

#设置测试报告标题
projectName = 'oms项目'
report_title = projectName  + u"测试报告"
#设置测试报告路径
report_path = os.path.abspath(os.path.join(os.getcwd(),'..')) + '\\test_report\\'
#获取系统当前时间
currentTime = time.strftime('%Y-%m-%d_%H%M%S',time.localtime(time.time()))

#设置报告名称
reportFile = report_path + currentTime + '.html'
# print(reportFile)

#判断是否存在test_report文件夹,不存在则创建
isExists = os.path.exists(report_path)
if not isExists:
    try:
        os.makedirs(report_path)
    except Exception as e:
        print("创建文件夹失败", e)

if __name__ == "__main__":
    with open(reportFile,"wb") as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=u"测试结果")
        runner.run(suite)






