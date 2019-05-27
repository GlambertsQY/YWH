import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    url = 'https://www.meijutt.com/content/meiju24451.html'
    response = requests.get(url, headers=headers)
    response.encoding = 'gb2312'
    with open('t.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find_all('div', attrs={'class': 'tabs-list'})
    # label = div.find('label', attrs={'class': 'down-ico current'})
    for i in div:
        print(str(i.prettify()))
    # print(label)
