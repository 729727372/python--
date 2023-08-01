#
# # 如何发起post 请求
# from urllib import request,parse
# data = {"phone": "8615896901897", "password": "qweqweqwe1", "oneMonth": "1"}
# data = parse.urlencode(data).encode('utf-8')
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"}
# '''构建请求对象'''
# req = request.Request(
#     url='http://dig.chouti.com/login',
#     data=data,
#     headers=headers
# )
# rep = request.urlopen(req)
# print(rep.read().decode("utf-8"))