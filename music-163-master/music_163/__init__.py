"""
__init__.py 用于告诉 Python 这个文件夹是一个 Python 的包
"""
import requests

if __name__ == '__main__':
    params = {
        'loginTicket': 'd441a504-9388-4659-a07b-455f21824c95',
        'username': '021116114',
        'password': '215838'
    }
    url = 'http://mids.sues.edu.cn/_customize/passLogin?service=http%3A%2F%2Fmy.sues.edu.cn%2F_web%2Fsopportal%2FteaIndex.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__'
    response = requests.get(url, params=params)
    print(response.url)
    print(response.cookies)
    print(response.text)
