# requests
# str -> JSON 데이터변환


import json
import requests


s = requests.Session()

# json 형태 데이터 요청
r = s.get('http://httpbin.org/stream/4', stream=True)
print(r.text)
print(r.encoding)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    print(line)
    print(type(line))

    b = json.loads(line) # str -> dict 변환
    print(b)
    print(type(b))

for k, v in b.items():
    print('key : {}, value : {}'.format(k,v))
    print('----')


r2 = s.get('http://jsonplaceholder.typicode.com/todos/1')
print(r2.headers)
print(r2.text)
print(r2.json())
print(r2.json().keys())
print(r2.json().values())

# 바이너리 정보
print(r2.content)
