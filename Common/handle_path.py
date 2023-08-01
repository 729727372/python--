import os
# 基础路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试用例路径
case_dir = os.path.join(base_dir,"Testcases")
# 测试数据路径
case_data = os.path.join(base_dir,"TestDateCases")
reports = os.path.join(base_dir,"reports")
conf_dir = os.path.join(base_dir,"Conf")
log_dir = os.path.join(base_dir,"OutPut\\log")
