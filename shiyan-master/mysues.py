import requests
from bs4 import BeautifulSoup


def get_headers():
    with open('headers.txt', 'r') as file:
        s = file.read()
    d = {}
    for i in s.split('\n'):
        d[i.split(':')[0].strip()] = i.split(':')[-1].strip()

    # del d['POST /login HTTP/1.1']
    del d['Cookie']
    del d['']
    return d


def get_data():
    formUrl = 'http://mids.sues.edu.cn/_customize/passLogin?service=http%3A%2F%2Fmy.sues.edu.cn%2F_web%2Fsopportal%2FstuIndex.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__'
    response = requests.get(formUrl)
    soup = BeautifulSoup(response.content.decode(), 'lxml')
    inputs = soup.form.find_all('input')

    datas = {}
    for i in range(0, 3):
        datas[inputs[i]['name'].strip()] = inputs[i]['value'].strip()

    datas['username'] = '021116114'
    datas['password'] = '215838'
    return datas


if __name__ == '__main__':
    headers = get_headers()
    data = get_data()
    host = 'http://mids.sues.edu.cn/_customize/passLogin?service=http%3A%2F%2Fmy.sues.edu.cn%2F_web%2Fsopportal%2FstuIndex.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__'
    response = requests.post(host, data=data, headers=headers)
    print(response.text)
