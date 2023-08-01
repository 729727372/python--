import pytest

from Common.handle_data import EnvData
from Common.handle_logger import logger

@pytest.fixture(scope="function")
def test_fixture():
    print("部分前置sssss")
    yield
    print("部分后置")
@pytest.fixture(scope="class")
def sql_fix():
    print("部分前置")
    yield
    print("部分后置")
@pytest.fixture(scope="function")
def env_del_data_dic():

    #  每次执行前清理EnvData s属性  防止出现BUG
    logger.info("每次执行前清理EnvData")
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)
    logger.info("清理EnvData完成{}".format(EnvData.__dict__))
