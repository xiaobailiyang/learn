# -*- coding:utf-8 -*-
# @author ：   liYang   
# @Time :    2019/5/23  9:12
import os
import unittest
import openpyxl
from HTMLTestRunnerNew import HTMLTestRunner
from day13.test_zy_day13 import RegisterTest

# test_path =os.path.dirname(os.path.abspath(os.path.relpath(__file__)))
#
# discover = unittest.defaultTestLoader.discover(test_path,  # 要测试的模块名或测试用例目录
#                                                pattern='test_*.py',  # 用例文件名的匹配原则，test开头
#                                                top_level_dir=None  # 顶层目录，如果没有顶层目录，默认为None
#                                                  )

suit = unittest.TestSuite()

#打开一个excel
wb = openpyxl.load_workbook('注册case.xlsx')
#获取所有sheet，是个列表,
sh = wb.sheetnames
print(sh)
#获取sheet
sheet = wb.active
#获取单元格的值
case_list = []
for case in list(sheet.rows)[1:]:
    case_d = {}
    case_d['data'] = case[1].value
    case_d['expected']= case[2].value
    case_list.append(case_d)

for i in case_list:
    suit.addTest(RegisterTest('test_register',eval(i['expected']),eval(i['data'])))

with open('report.html','wb') as f:
    runner = HTMLTestRunner(stream=f,   #报告文件名称
                            verbosity=2,    #报告详细级别
                            title='这是第一个标题',    #报告标题
                            description='这是第一份报告的描述',   #报告描述
                            tester='test_01')   #报告者
    runner.run(suit)


wb.close()