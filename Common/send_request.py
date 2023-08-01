import requests
from Common.handle_logger import logger

class RequestUtil:

    def send_reqest(self,method,url,date,**kwargs):
        method = str(method).lower()
        res = None
        if method == "get":
            res = requests.get(url=url,params=date)
            logger.info(res.json())

        elif method == "post":
            res = requests.post(url=url,json=date)
            logger.info(res.json())
        else:
            print("不在请求范围内")
        return res


# import requests
#
# class HttpRequest:
#     def __init__(self, base_url):
#         self.base_url = base_url
#
#     def get(self, url, params=None, headers=None, **kwargs):
#         response = requests.get(self.base_url + url, params=params, headers=headers, **kwargs)
#         return response
#
#     def post(self, url, data=None, json=None, headers=None, **kwargs):
#         response = requests.post(self.base_url + url, data=data, json=json, headers=headers, **kwargs)
#         return response
#
#     def put(self, url, data=None, json=None, headers=None, **kwargs):
#         response = requests.put(self.base_url + url, data=data, json=json, headers=headers, **kwargs)
#         return response
#
#     def delete(self, url, headers=None, **kwargs):
#         response = requests.delete(self.base_url + url, headers=headers, **kwargs)
#         return response

