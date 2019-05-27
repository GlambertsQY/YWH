import requests
import time
import random
import threading
import logging

cookies0 = {'wsess': 'ST-22654-t0M2ih9PcQU2sp6HvjBP1558949701728-l1d2-ids1'}
cookies1 = {'wsess': 'ST-22595-gNqtqC5kJgOmEcJiOMkG1558949011846-l1d2-ids1'}


def shiyan(cookies, user):
    print(str(user) + ' start...')
    logging.error(user + ' start...')
    # loginUrl = 'http://202.121.126.68/exam_login.php'
    # loginData = {'xuehao': '20161593', 'password': '214122', 'postflag': '1', 'cmd': 'login', 'role': '0'}
    # login = requests.post(loginUrl, data=loginData)
    # cookies = dict(wsess=login.cookies['wsess'])
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'charset': 'UTF-8', 'Content-Length': '16',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    heartBeatUrl = 'http://labsafe.shiep.edu.cn/exam/exam_xuexi_online.php'
    heartBeatData = {'cmd': 'xuexi_online'}

    hearBeat = requests.post(heartBeatUrl, heartBeatData, headers=headers, cookies=cookies)
    if dict(hearBeat.json())['status'] == 1:
        while (dict(hearBeat.json())['shichang'][:2] != '4时'):
            hearBeat = requests.post(heartBeatUrl, heartBeatData, headers=headers, cookies=cookies)
            logging.error('xuehao=%s, json=%s\n', user, hearBeat.json())
            time.sleep(random.uniform(50, 70))
        print(str(user) + ' end successfully...')
    else:
        print(str(user) + ' end with status 0...')


if __name__ == '__main__':
    threadpool = []
    th = threading.Thread(target=shiyan, args=(cookies0, '20161593'))
    threadpool.append(th)
    th = threading.Thread(target=shiyan, args=(cookies1, '20161600'))
    threadpool.append(th)

    # for xh in range(0, 2):
    #     th = threading.Thread(target=shiyan, args=())
    #     threadpool.append(th)

    for th in threadpool:
        th.start()
    for th in threadpool:
        threading.Thread.join(th)
