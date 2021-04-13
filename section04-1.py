# Requests 모듈 사용
# session 사용


import requests

# s = requests.Session()
# r = s.get('http://www.naver.com')

# print(r.status_code)
# print(r.ok)
# s.close()


# httpbin 사이트 response
ss = requests.Session()
cookie = ss.get('https://httpbin.org/cookies', cookies={'name':'chanjoolee'})
print(cookie.text)


url = 'https://httpbin.org'
headers = {'user-agent': 'crawler'}

r3 = ss.get(url, headers=headers)
print(r3.text)

# with문 사용 권장 :
# 외부에 리소스를 요청할 때 (파일, DB, HTTP)
# session.close() 자동 반환해줌

with requests.Session() as s:
    r = s.get('http://www.daum.net')
    print(r.text)
    print(r.ok)
