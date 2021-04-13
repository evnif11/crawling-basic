# REST API 를 requests 모듈에서 지원함
# 웹에 리소스 요청하는 것을 자유자재로

# REST api : GET / POST / DELETE / PUT /
#            REPLACE(FETCH : UPDATE, MODIFY)
# URL만 보고도 자원 상태 정보를 알 수 있음


import requests


s = requests.Session()

r = s.get('http://api.github.com/events')

# 수신상태 체크
r.raise_for_status()
print(r.text)


# 쿠키설정
jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'niceman', domain='httpbin.org', path='/cookies')
r = s.get('https://httpbin.org/cookies', cookies=jar)
print(r.text)


# 타임아웃을 줄 수 있음
r = s.get('http://github.com', timeout=4)
print(r.text)

# POST (1)
r = s.post('https://httpbin.org/post', data={'id':'test', 'pw':'1111'}, cookies=jar)
print(r.text)
print(r.headers)


# POST (2)
payload1 = {'id':'test', 'pw':'1111'}
payload2 = (('id','test'),('pw','0000'))

r = s.post('https://httpbin.org/post', data=payload1)
print(r.text)


# PUT
r = s.post('https://httpbin.org/put', data=payload2)
print(r.text)
