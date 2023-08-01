
import pytest
from Common.handle_logger import logger

@pytest.mark.smoke
@pytest.mark.usefixtures("sql_fix")
class TestThree:
    def test_ces(self):
        logger.info("TestThree开始执行")
        print("测试类的部分前置")
        logger.info("TestThree执行结束")
    @pytest.mark.xfail
    def test_one(self):
        logger.info("TestThree开始执行")
        print("测试类的部分前置")
        logger.info("TestThree执行结束")
        assert 1==2