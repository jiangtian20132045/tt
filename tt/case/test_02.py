# coding:utf-8
import unittest
import requests
class Test_Kuaidi(unittest.TestCase):
    def setUp(self):
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
        } # get方法其它加个ser-Agent就可以了
        self.s = requests.session()

    def test_yunda(self):
        danhao = '1202247993797'
        kd = 'yunda'
        # 这里对url的单号参数了
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao, kd)
        print(self.url)
        # 第一步发请求
        r = self.s.get(self.url, headers=self.headers, verify=False)
        result = r.json()
        # 第二步获取结果
        print(result['company']) # 获取公司名称
        data = result["data"] # 获取data里面内容
        print(data[0]) # 获取data里最上面有个
        get_result = data[0]['context'] # 获取已签收状态
        print(get_result)
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"韵达快递", result['company'])
        self.assertIn(u"已签收", get_result)


    def test_tiantian(self):
        danhao = '560697415000'
        kd = 'tiantian'
        # 这里对url的单号参数了

        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" % (danhao, kd)
        print(self.url)
        # 第一步发请求
        r = self.s.get(self.url, headers=self.headers, verify=False)
        result = r.json()
        # 第二步获取结果
        print(result['company'])  # 获取公司名称
        data = result["data"]  # 获取data里面内容
        print(data[0])  # 获取data里最上面有个
        get_result = data[0]['context']  # 获取已签收状态
        print(get_result)
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"天天快递", result['company'])
        self.assertIn(u"已签收", get_result)

    if __name__ == "__main__":
        unittest.main()
