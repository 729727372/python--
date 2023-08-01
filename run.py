import os
import time

import pytest

if __name__ == '__main__':
    pytest.main(['-s'])
    # pytest.main(["-k","test_01_get_token"])
    time.sleep(1)
    os.system("allure generate ./temp -o ./reports --clean")
