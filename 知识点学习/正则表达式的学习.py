import re
# 定义一个字符串
text = "Hello, my name is John Doe. I am 30 years old.name"
a = {
    "name":"张三",
    "age":14
}
ss = str(a)
# 定义一个正则表达式，匹配所有的单词
pattern = r'age":/d'

# 使用findall方法查找所有匹配的单词
result = re.findall(pattern, ss)

# 输出结果
print(result)