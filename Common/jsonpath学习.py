

import jsonpath


resp = {

    "code":"0",
    "data":{
        "token":"111111",
        "id":"20"
    }
}

res = jsonpath.jsonpath(resp,"$.data.id")[0]
print(res)

url = "http://api.lemonban."