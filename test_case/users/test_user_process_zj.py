import random

import allure
import requests

from config.conf import API_URL

@allure.feature("用户管理")
@allure.story("充值提现模块")
@allure.title("扣款接口-账户余额不足")
def test_re(pub_data,db):
    with allure.step("第一步,执行SQL语句"):
       res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL ;")
    with allure.step("第二步,从查询结果中随机获取一条,取第一个数据"):
       account_name = random.choice(res)[0]
    with allure.step("第三步,准备请求数据"):
       data = {
  "accountName": account_name,
  "changeMoney": 100
}
    with allure.step("第四步,发送请求"):
           r = requests.post(API_URL + "/acc/recharge",json=data)
    with allure.step("第五步,获取请求内容"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求URL", allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头", allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求正文", allure.attachment_type.TEXT)
    with allure.step("第六步,获取请求内容"):
        allure.attach(str(r.status_code),"响应状态码", allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响应头", allure.attachment_type.TEXT)
        allure.attach(r.text, "响应正文", allure.attachment_type.TEXT)
    with allure.step("第七步,断言"):
        allure.attach(r.text, "实际结果", allure.attachment_type.TEXT)
        allure.attach("2000", "预期结果", allure.attachment_type.TEXT)
        assert "2000"







'''
   pytest test_case/users/test_user_process_zj.py --alluredir=reports/xml
   allure generate reports/xml -o reports/html
   allure generate reports/xml -o reports/html --clean
   '''
