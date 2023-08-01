
from openpyxl import load_workbook
import os

class Openpy:
    def __init__(self,filename,sheetname):
        self.wk = load_workbook(filename)
        self.sh = self.wk[sheetname]
    # 获取excel 标题列表
    def read_title(self):
        title = []
        for lineone in list(self.sh.rows)[0]:
            title.append(lineone.value)
        return title
    # 获取全部数据列表
    def alldates(self):
        title = self.read_title()
        alldates= []
        for item in list(self.sh.rows)[1:]:
            new_dic = {}
            for index in range(len(item)):
                new_dic[title[index]] = item[index].value
            alldates.append(new_dic)
        return alldates
    def close_file(self):
        self.wk.close()



