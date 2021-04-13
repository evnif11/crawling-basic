# 다음 주식 정보 가져오기
# Fake-useragent 사용
# header 직접 작성해보기




import json
from urllib import request
from fake_useragent import UserAgent

# fake header 정보
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)


headers = {
    'User-agent' : ua.ie,
    'referer': "https://finance.daum.net/"
}

url = 'https://finance.daum.net/api/search/ranks?limit=10'

res = request.urlopen(request.Request(url, headers=headers)).read().decode('utf-8')
# print(res)


rank_json = json.loads(res)['data']
print(rank_json)

for elm in rank_json:
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm.get('tradePrice'), elm['name']))
