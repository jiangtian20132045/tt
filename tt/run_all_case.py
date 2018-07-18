#coding:utf-8
import unittest
import os
from report import HTMLTestRunner_TT
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# base_dir = str(os.path.dirname(os.path.dirname(__file__)))
# base_dir = str(os.path.dirname(os.path.realpath(__file__)))
# cur_path = base_dir.replace("\\","/")
cur_path = str(os.path.dirname(os.path.realpath(__file__)))
# print(base_dir)
print(cur_path)
def add_case(caseName="case",rule="test*.py"):
    #待执用例的目录
    # case_dir = "C:\\Users\\Administrator\\PycharmProjects\\oldrequest\\case"
    #第一步:加载所有的测试用例
    #用例文件夹
    case_path = os.path.join(cur_path,caseName)
    if not os.path.exists(case_path):
        os.mkdir(case_path)
        print("test case path:%s"%case_path)
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    print(discover)
    return discover

    # case_dir = base_dir+"/case/"
    # print(case_dir)
    # testcase = unittest.TestSuite()

    # discover = unittest.defaultTestLoader.discover(case_dir,
    #                                                pattern="test*.py",
    #                                                top_level_dir=None)

    #discover方法筛选出来的用例，循环添加到测试套件中
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         #添加用例到testcase
    #         testcase.addTests(test_case)
    #     print(testcase)
    # return testcase

def send_email():
    # --1.跟发邮件相关的参数--
    # 发件服务器
    #企业邮箱的服务，如果是个人就用smtp.163.com
    smtpsever = "smtp.qiye.163.com"
    # 端口 port
    port = 0
    #账号
    sender = "tjiang@grandstream.cn"
    #密码
    psw = "grandstream@jia1"
    #接收人(多个收件人时采用list对象)
    receiver = ["772831364@qq.com","1026437653@qq.com"]

    #--2.这里是邮件的内容

    fire_path = cur_path+"\\report\\result.html"
    with open(fire_path,'rb') as fp:
        mail_body = fp.read()
        # fp.close()
    msg = MIMEMultipart()

    subject = "这个是主题666"
    msg['form'] = sender
    #多个收件人时，recevier是list，但是这个字典中需要的类型是字符串
    msg['to'] = (";").join(receiver)
    print((";").join(receiver))
    msg['subject'] = subject
    #定义邮件正文为html格式
    #正文
    body = MIMEText(mail_body,"html","utf-8")
    #附件
    att = MIMEText(mail_body,'base64','utf-8')
    att["Content-Type"]  = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="result.html"'
    msg.attach(body)
    msg.attach(att)
    print("test email is send")

#--3.发送邮件
    try:
        smtp = smtplib.SMTP()
    #连接服务器
        smtp.connect(smtpsever)
        #登录
        smtp.login(sender,psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpsever,port)
        smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

#生成html报告
def run_case(all_case,reportName="report"):
    """"第二步:执行所有的用例，并把结果写入HTML测试报告"""
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    #用例文件夹
    report_path = os.path.join(cur_path,reportName)
    #如果不存在就自动创建一个
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path+"\\result.html")
    print(report_path)
    print("report path: %s"%report_abspath)
    fp = open(report_abspath, "wb")
    # runnrer = unittest.TextTestRunner()
    # run所有用例
    runnrer = HTMLTestRunner_TT.HTMLTestRunner(stream=fp,
                                               title="这是我的自动化测试报告",
                                               description="用例执行情况",
                                               TT_name="jiangtian")
    runnrer.run(all_case)
    fp.close()

# def get_report_file(report_file):
#     #获取最新的测试报告

if __name__ == "__main__":
        #返回实例
        # report_path = base_dir+"/result.html"
        # fp = open(report_path,"wb")
        # runnrer = unittest.TextTestRunner()
        #run所有用例
        # runnrer = HTMLTestRunner_TT.HTMLTestRunner(stream=fp,
        #                                            title="这是我的自动化测试报告",
        #                                            description="用例执行情况",
        #                                            TT_name="jiangtian")
        # runnrer.run(add_case())
        # fp.close()
        #加载用例
        all_case = add_case()
        #执行用例
        run_case(all_case)
        #获取最新生成的测试报告文件
        report_path = os.path.join(cur_path,"report")
        send_email()