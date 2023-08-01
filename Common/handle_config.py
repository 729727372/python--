from configparser import  ConfigParser
from Common.handle_path import conf_dir
import os
class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding="utf-8")
file_path = os.path.join(conf_dir,"conf.ini")

config = HandleConfig(file_path)


print(config.get("log","name"))
