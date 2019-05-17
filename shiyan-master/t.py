import requests
import pytesseract
from PIL import Image

if __name__ == '__main__':
    headers = {
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Host': 'jxxt.sues.edu.cn',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'Referer': 'http://jxxt.sues.edu.cn/eams/defaultHome.action?method=moduleList&parentCode=',
        'Upgrade-Insecure-Requests': '1'
    }

    img_url = 'http://jxxt.sues.edu.cn/eams/captcha/image.action'

    imgresponse = requests.get(img_url, headers=headers)
    with open('t.gif', 'wb') as img:
        img.write(imgresponse.content)
    img = Image.open('t.gif', 'r')
    code = pytesseract.image_to_string(img)

    params = {
        'loginForm.name': '021116114',
        'loginForm.password': '215838',
        'encodedPassword': '',
        'loginForm.captcha': code
    }

    hosturl = 'http://jxxt.sues.edu.cn/eams/login.action'
    response = requests.post(hosturl, data=params, cookies=requests.utils.dict_from_cookiejar(imgresponse.cookies),
                             headers=headers)
    # cookies = requests.utils.dict_from_cookiejar(response.cookies)
    # cookies.update(poped=' ')
    #
    # url = 'http://jxxt.sues.edu.cn/eams/personGrade.action'
    # response = requests.get(url, cookies=cookies, headers=headers)

    with open('t.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print(response.url)
    print(response.request.headers)
