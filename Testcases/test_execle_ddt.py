
import  unittest
import os

import pytest
from ddt import ddt ,data

from Common.handle_openpyxl import Openpy
from Common.handle_logger import logger
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parent_dir = os.path.join(current_dir, 'TestDateCases\logincases.xlsx')

open = Openpy(parent_dir,"login")
cases = open.alldates()

@pytest.mark.parametrize("cases", cases)
def test_login(cases):
    print("开始执行",cases["username"],cases["password"],cases["check"])
    logger.info(cases)
    for key,value in cases.items():
        print(key,value)
if __name__ == '__main__':
    pytest.main(["-vs"])