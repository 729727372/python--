import json
import re
from Common.handle_config import config
class EnvData:
    # 存储全局变量   可以通过类直接访问   setattr(EnvData,"name","zhangsan")  EnvData.name 获取值
    pass


def replace_by_regular_dict(case):
    '''
    :param case: 从execl读取的用例,做全部替换
    包括URL  request_Data expected check_sql
    :return:
    '''
    case_str = json.dumps(case)
    new_case = replace_by_regular(case_str)
    case_dic = json.loads(new_case)
    return case_dic

def replace_by_regular(data):
    '''
    :param data:data 字符串  匹配#(.*?)#  替换真实数据   数据来源于EnvData 和  配置文件单子
    :return:  返回的是替换之后的字符串
    '''
    res = re.findall("#(.*?)#", data)
    if res:
        for item in res:
            try:
                vaule = getattr(EnvData, item)
            except:
                try:
                    vaule = config.get("data", item)
                except AttributeError:
                    continue
            data = data.replace("#{}#".format(item), vaule)
    return data