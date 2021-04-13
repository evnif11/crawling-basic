# beautiful soup
# 로그인 기능 추가해서

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


# 로그인 폼 정보
login_info = {
    'loginMemberType': 'general',
    'id': 'dlckswn14',
    'isSaveId': 'true',
    'password': 'asd51364243!!'
}

# Headers 정보
headers = {
    "User-Agent": UserAgent().chrome,
    # login referer 넣어주기
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F"
}

with requests.session() as s:
    # request url 넣어줘야해
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)

    if res.status_code != 200:
        raise Exception('login failed')

    # print(res.content.decode('utf-8'))
    # Euc-kr(한글 깨질 경우)
    # res.encoding = 'euc-kr'


    # 로그인 성공 후 세션 정보 가지고 페이지 이동
    res = s.get('https://www.danawa.com/member/myPage.php', headers=headers)
    # print(res.text)

    # bs 초기화
    soup = BeautifulSoup(res.text, 'html.parser')

    # 로그인 성공 체크
    check_name = soup.find('p', class_='p_nick')
    print(check_name)
    print(check_name.text)

    if check_name.text == '님':
        raise Exception('로그인 실패했음. 비번 틀림.')


    info_list = soup.select("div.state_bg > ul.state_list > li")
    print(info_list)

    for v in info_list:
        proc = v.find('h4').string.strip()
        val = v.find('strong').string.strip()

        print(proc, val)
