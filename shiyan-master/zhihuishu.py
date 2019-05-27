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
    formUrl = 'https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/'
    response = requests.get(formUrl)
    soup = BeautifulSoup(response.content.decode(), 'lxml')
    inputs = soup.form.find_all('input')
    datas = {}
    for i in range(0, 5):
        datas[inputs[i]['name'].strip()] = inputs[i]['value'].strip()

    datas['username'] = '1762563117'
    datas['password'] = 'abc123456'
    return datas


if __name__ == '__main__':
    # data = get_data()
    headers = get_headers()
    print(headers)

    data = {
        'recruitAndCourseId': '4b585f584652415846425f5d5a'
    }
    cookie = {
        'Cookie': 'assess_criteria_toggle_10603=on; Hm_lvt_0a1b7151d8c580761c3aef32a3d501c6=1558339123,1558339134; o_session_id=37F4F3EEE43F15BADD227A73AF66ABAA; Z_LOCALE=1; acw_tc=76b20ff915583392893586064e53d4b3bc599427da1627f40e92d06690dc9e; route=44eb826555c101c3072641d0d2b6c21c; c_session_id=5E01C1371109645835DDDF8AE4788721; isLogin=myschool; cookieServer=1; warningTip=1; zsh_learning_rid_10603_userId_196464993_videoId_142413=2_307.5_00%3A04%3A53; ZHSID=BF836EDC46CD8FF2CFCDAE0CAA644B18; privateCloudSchoolInfo_196464993=",1,#0f0c1d,http://image.zhihuishu.com/testzhs/myuni/home/201607/5c40c1f661034427a0fb454d73d65d29.png,http://image.zhihuishu.com/zhs/myuni/home/201712/b617b9b6cbe24fd5939bfd724f18f264.png,19,http://school.zhihuishu.com/sues,"; zsh_learning_rid_10603_userId_196464993_videoId_158225=2_277.5_00%3A04%3A24; CASLOGC=%7B%22myuniRole%22%3A0%2C%22username%22%3A%22e376bc3b24c7466b844de8bd54296371%22%2C%22mycuRole%22%3A0%2C%22userId%22%3A196464993%2C%22myinstRole%22%3A0%2C%22realName%22%3A%22%E6%9D%A8%E6%96%87%E8%B1%AA%22%2C%22uuid%22%3A%22VBRGBM14%22%2C%22headPic%22%3A%22http%3A%2F%2Fimage.zhihuishu.com%2Fzhs%2Fablecommons%2Fdemo%2F201804%2Fdacc8bdfb6c7492ca32dfe37441842f9_s3.jpg%22%7D; CASTGC=""; JSESSIONID=0043D12C76F7DAE942D1462EDB8BA731; Hm_lpvt_0a1b7151d8c580761c3aef32a3d501c6=1558508546; SERVERID=4516a494fea80bcfc392e5b45dea0690|1558508549|1558508543'
    }
    loginurl = 'http://study.zhihuishu.com/learning/videoList'
    response = requests.post(loginurl, data=data, headers=headers, cookies=cookie)
    print(response.url)
    print(response.cookies)
    with open('zhihuishu.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
