# -*- coding:utf-8 -*-
# @author ：   liYang   
# @Time :    2019/5/21  9:47

import unittest
import os
from  day13.register import register


class RegisterTest(unittest.TestCase):
    def setUp(self):
        print('测试开始之前的准备环境')

    def tearDown(self):
        print('测试结束之后恢复环境')

    def test_register_success(self):
        '''正确的用户名、密码，注册工程'''
        exce ={"code": 1, "msg": "注册成功"}
        data=('python180','biaoqing','biaoqing')
        result = register(*data)
        try:
            self.assertEqual(exce,result,msg='断言成功')
        except AssertionError as e:
            raise e
        else:
            print('注册成功')

    def test_password_different(self):
        '''正确的用户名，两次密码不一样，注册失败'''
        exce = {"code": 0, "msg": "两次密码不一致"}
        data = ('112233','112233','112244')
        result = register(*data)
        try:
            self.assertEqual(exce,result,msg='断言失败')
        except AssertionError as e:
            raise e
        else:
            print('两次密码不一样，测试成功')

    def test_password_short(self):
        '''正确的账号，密码长度少于6个字符'''
        exce = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        data = ('xiaobai','12','12')
        result = register(*data)
        try:
            self.assertEqual(exce,result,msg='断言失败')
        except AssertionError as e:
            raise e
        else:
            print('密码长度少于6个字符，测试成功')

    def test_username_repeat(self):
        '''用户名重复'''
        exce = {"code": 0, "msg": "该账户已存在"}
        data = ('python18','1234567','1234567')
        result = register(*data)
        try:
            self.assertEqual(exce,result,msg='断言失败')
        except AssertionError as e:
            raise e
        else:
            print('用户名，已存在，测试成功')

    def test_username_short(self):
        '''用户名长度少于6个字符'''
        exce = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        data = ('short','12345678','12345678')
        result = register(*data)
        try:
            self.assertEqual(exce,result,msg='断言失败')
        except AssertionError as e:
            raise e
        else:
            print('用户名长度少于6个字符，测试成功')

    def test_username_long(self):
        '''用户名大于18个字符'''
        exce = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        data = ('toolong','1234567890123456789','1234567890123456789')
        result = register(*data)
        try:
            self.assertEqual(exce,result,msg='断言失败')
        except AssertionError as e:
            raise e
        else:
            print('用户名大于18个字符,测试成功')


if __name__ == '__main__':
    '''
    #1、根据case名称，加载
    unittest.main()
    #2、1.构建测试套件
    suit = unittest.TestSuite()
    suit.addTest(RegisterTest('test_register_success'))
    suit.addTest(RegisterTest('test_password_different'))
    suit.addTest(RegisterTest('test_password_short'))
    suit.addTest(RegisterTest('test_username_repeat'))
    suit.addTest(RegisterTest('test_username_short'))
    suit.addTest(RegisterTest('test_username_long'))
    #2.2 实例化TextTestRunner类
    runner =unittest.TextTestRunner()
    #2.3 运行case
    runner.run(suit)
    '''
    #3、 discover
    test_path = os.path.relpath(__file__)
    discover = unittest.defaultTestLoader.discover(test_path, #要测试的模块名或测试用例目录
                                                   pattern='test_*.py',#用例文件名的匹配原则，test开头
                                                   top_level_dir=None  #顶层目录，如果没有顶层目录，默认为None
                                                   )
    runner = unittest.TextTestRunner()
    runner.run(discover)

