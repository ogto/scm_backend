import requests


def send_request(url, method, header, data=''):
    _header = header

    if method == "GET":
        res = requests.get(url, headers=_header)
    elif method == "POST":
        res = requests.post(url, data=data, headers=_header)
    elif method == "PUT":
        res = requests.put(url, data=data, headers=_header)
    elif method == "DELETE":
        res = requests.delete(url, data=data, headers=_header)
    else:
        return

    print(str(res.status_code) + " | " + res.text)
    return res
