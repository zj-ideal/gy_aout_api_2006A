import random

import allure
import pytest
from tools.api import request_tool
from tools.data import excel_tool

data = excel_tool.get_test_case("test_case/users/测试用例工作表(2)(1).xls")


@pytest.mark.parametrize("accountName,changeMoney,expect", data[1], ids=data[0])
def test_recharge(pub_data,accountName,changeMoney,expect):
    pub_data["accountName"] = accountName
    pub_data["changeMoney"] = changeMoney
    method = "POST"  # 请求方法，全部大写
    feature = "yonghu"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    uri = "/acc/recharge"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
               'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084',
               'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis',
               'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = expect  # 预期结果
    json_data = '''{
  "accountName": "${accountName}",
  "changeMoney": "${changeMoney}"
}
'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, json_data=json_data)

# @allure.feature("一级分类")
# @allure.feature ("二级分类").
# @allure.title("用例标题")
def str9(headers):
    pass


def test_recharge(pub_data, db, r=None):
    with allure.step("第一步、执行sql语句"):
        res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL;")
        pub_data["account_name"]=random.choice(res)[0]  # random.choice随机取值
        method = "POST"  #请求方法，全部大写
        feature = "用户模块"  # allure报告中一级分类
        story = '用户登录'  # allure报告中二级分类
        title = "全字段正常流_1"  # allure报告中用例名字
        uri = "/acc/recharge"  # 接口地址
        headers = {"token":pub_data["token"]}
        status_code = 200  # 响应状态码
        #allure.attach(r.text,"响应正文 ",allure.attachment_type.TEXT)#str()转成字符串
    expect = ""  # 预期结果allure.attach("", "预期结果 ",allure.attachment_type.TEXT)
    json_data='''{
  "accountName": "${accountName}",
  "changeMoney": 12
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)