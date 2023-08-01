import logging
import os.path

from Common.handle_config import config
from Common.handle_path import log_dir

class Mylogger(logging.Logger):
    def __init__(self,file = None):
        # 设置输出级别，输出日志格式
        super().__init__(config.get("log","name"),config.get("log","level"))

        # 日志模式输出格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line: %(message)s'
        formatter = logging.Formatter(fmt)

        # 将日志绑定到渠道中
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            handle2 = logging.FileHandler(file,encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

# 是否需要引入文件
if config.getboolean("log","file_ok"):
    print("执行到了")
    file_name = os.path.join(log_dir,config.get("log","file_name"))
else:
    file_name = None
print(file_name)
logger = Mylogger(file_name)
