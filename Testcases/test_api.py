import jsonpath
import pytest

from Common.yaml_util import YamlUtil
from Common.send_request import RequestUtil
from Common.handle_logger import logger
from Common.handle_data import EnvData
import requests
class TestApi:

    @pytest.mark.usefixtures("env_del_data_dic")
    @pytest.mark.parametrize("caseinfo",YamlUtil().read_yaml('get_token.yml'))
    def test_01_get_token(self,caseinfo):
        logger.info("获取到的用例{}".format(caseinfo))
        method = caseinfo['request']['method']
        logger.info("请求的方法是{}".format(method))
        url = caseinfo['request']['url']
        logger.info("请求的URL{}".format(url))
        date = caseinfo['request']['date']
        setattr(EnvData,"data",date)
        logger.info("全局变量data:{}".format(EnvData.data))
        request = RequestUtil()
        res = request.send_reqest(method=method,url=url,date=date)
        logger.info("响应结果是:{}".format(res.json()))
        code = res.status_code
        dic = res.json()
        logger.info("dic的内容是",dic)
        # logger.info("access_token值是{}".format(dic["access_token"]))
        setattr(EnvData,"access_token","暂时写死的")

        logger.info("接口返回结果是{}".format(res.json()))
        logger.info("EnvData全局变量存储的的access_token：{}".format(EnvData.access_token))
        assert 200 == code

        # logger.info("返回的status_code")

    # @pytest.mark.parametrize("caseinfo", YamlUtil().read_yaml('get_token.yml'))
    # def test_01_get_token(self, caseinfo):
    #     print(caseinfo)
    #     print(caseinfo['name'])
    #     method = caseinfo['request']['method']
    #     url = caseinfo['request']['url']
    #     date = caseinfo['request']['date']
    #     print(caseinfo['validate'])
    #     res = RequestUtil().send_reqest(method,url,date)
    #     print(res.json())

    # @pytest.mark.parametrize("name,age", [['百里','12'],['依然','13']])
    # def test_02_get_token(self, name,age):
    #     print("获取token值:" +  name,age)