import requests


url = "https://api.weixin.qq.com/cgi-bin/token"

data = {

    "appid":"wx6b11b3efd1cdc290",
    "secret":"106a9c6157c4db5f6029918738f9529d",
    "grant_type":"client_credential"
}
res = requests.get(url,params=data)

print(res.json())
