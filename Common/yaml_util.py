import os
import yaml
class YamlUtil:
    def read_yaml(self,yaml_name):
        with open(os.getcwd()+"/Testcases/test_yml/"+yaml_name,encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            print("value",value)
            return value


