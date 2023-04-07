#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class A:
#     def __init__(self):
#         self.n = 1
#
#     def add(self, m):
#         print(f'AAA [self] is {id(self)}')
#         print(f'AAA [self.n] is {self.n}')
#         self.n += m
#
#
# class B(A):
#     def __init__(self):
#         self.n = 100
#
#     # 重写父类方法
#     def add(self, m):
#         # 子类特有代码
#         print(f'BBB [self] is {id(self)}')
#         print(f'BBB [self.n] is {self.n}')
#         print({id(self)})
#
#         # 调用父类方法
#         super().add(m)
#
#         self.n += m
#
#
# b = B()
# b.add(2)
# print(b.n)




import unittest
from common.canshu import Merge,random_name
from common.CPS_login import login
from common.mylogin import mylogin
import requests
from common.config import Conf
import json


# class Me(unittest.TestCase):
#     u"""我的页面数据接口"""
#     def setUp(self):
#         self.url = 'https://shop-nn.oss-cn-hangzhou.aliyuncs.com/images/goods/video/349380247187817.mp4'
#     def test_a_getuserinfo(self):
#         u"""获取个人信息数据"""
#         data = {
#             'url':self.url
#         }
#         response = requests.post(url='http://yijianxiaopusystemnew.nnnmn178.com/sys/douyin/goods/videoClip.shtml')
#         result = json.loads(response.content)
#         # print(result)
#         return result
#
#
# if __name__ == '__main__':
#     unittest.main()


class Me(unittest.TestCase):
    u"""我的页面数据接口"""
    def setUp(self):
        self.url = 'http://yijianxiaopuapi.nnnmn178.com/yxrweb/douYin/getActivityImage'
    def test_a_getuserinfo(self):
        u"""获取个人信息数据"""
        data = {
            'url':self.url
        }
        response = requests.post(url=self.url,data=data)
        result = json.loads(response.content)
        print(result)
        # return result


if __name__ == '__main__':
    unittest.main()







