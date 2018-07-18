#coding:utf-8
from bs4 import BeautifulSoup
import requests

# r = requests.get("http://www.cnblogs.com/yoyoketang")
# #请求后获取整个页面
# result = r.content
# print(result)
#
# #用html.parser解析html
# soup = BeautifulSoup(result,"html.parser")
#
# #获取所有的class属性为dayTitle,返回tag类
# times = soup.find_all(class_="dayTitle")
# for i in times:
#     a = i
#     print(i.a.string)

yoyo = open("tt.html",encoding='gbk',errors='ignore')
soup = BeautifulSoup(yoyo)
print(soup.prettify())
