# GET 방식 데이터 통신

import urllib.request
from urllib.parse import urlparse

# url = "http://www.encar.com"

# # urlopen 함수 이용해서 변수에 수신된 정보 저장 가능
# car = urllib.request.urlopen(url)

# # urlopen을 이용한 메소드들
# print(type(car))
# print(car.geturl())
# print(car.status)
# print(car.getcode())
# print(car.getheaders())
# print(car.read(100))

# # urlparse: URL을 분리해줌
# print(urlparse("http://www.encar.com?test=test"))



api = "http://api.ipify.org"

values = {
    'format': 'json'
}

# urlencode : 제이슨 형태의 데이터를 번역해줌
params = urllib.parse.urlencode(values)
print(params)

# 요청 url 생성
URL = api + '?' + params
print(URL)

data = urllib.request.urlopen(URL).read()
print(data.decode('utf-8'))
