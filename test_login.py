import random
# # http://yijianxiaopusystemnew.nnnmn178.com/login/save.shtml
# import unittest
# from common.canshu import Merge,random_name
# from common.CPS_login import login
# from common.mylogin import mylogin
# import requests
# from common.config import Conf
# import json
#
#
# class Me(unittest.TestCase):
#     def test_a_getuserinfo(self):
#
#         headers = {
#         'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
#         'Accept': 'text/html, application/xhtml+xml, */*'
#
#     }
#         data = {
#             'password':'Rjp123456',
#             'userName':'15037431008'
#         }
#         response = requests.post(url='http://yijianxiaopusystemnew.nnnmn178.com/login/save.shtml',data=data,headers=headers,verify=False)
#         print(response)
#         result = json.loads(response.content)
#         print(result)
#         return result
#
#
# if __name__ == '__main__':
#     unittest.main()



# ning = '\n'.join([''.join([('love'[(x-y) % len('love')]
#                             if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')
#                            for x in range(-30, 30)]) for y in range(30, -30, -1)])
# print("\033[5;31;40m%s\033[0m" % ning)


# a = [1,2,3,4,5,6,7,8,9,10]
#
# print(a[3:7])


# 求1-100的和
a = 0
for i in range(101):
        a=a+i
print(a)

# 求1-100偶数的和
b = 0
for i in range(101):
    if i%2==0:
        b=b+i
print(b)

c = 0
for i in range(2,101,2):
    c=c+i
print(b)


#随机一个数字，然后猜测大一点  小一点  相等

# ab = 39
cd = random.randint(1,100)
print(cd)
while True:
    ab = int(input('请输入一个数字:'))
    if ab>cd:
        print("大一点")
    elif ab<cd:
        print('小一点')
    elif ab==cd:
        print('猜对了')





y = lambda x,y,z:x+y+z
print(y(1,2,3))















