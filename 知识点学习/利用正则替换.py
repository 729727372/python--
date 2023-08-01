import re
from Common.handle_data import EnvData
from Common.handle_config import config

setattr(EnvData,"member_id","11111222222")
setattr(EnvData,"amount_id","11111222223")

def replace_by_regular(data):
    res = re.findall("#(.*?)#", data)
    if res:
        for item in res:
            try:
                vaule = getattr(EnvData, item)
            except:
                vaule = config.get("data", item)
            data = data.replace("#{}#".format(item), vaule)
    return data
data = '{"member_id":"#member_id#","amount_id":"#amount_id#","money":"#user_money#"}'
res = replace_by_regular(data)
print(res)