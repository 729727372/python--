


def replace_mark_realmark(case,mark,realmark):
    # case 是字典形式
    for key,value in case.items():
        if value is not None and isinstance(value,str):
            if value.find(mark) != -1:
                case[key] = realmark
    return case


if __name__ == '__main__':
    case = {"name":"zhangsan","age":"sss"}
    ss = replace_mark_realmark(case,"sss","aaa")
    print(ss)

