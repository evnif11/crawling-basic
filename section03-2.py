# RSS 주소 이용해
# xml 형태로 데이터 받을 수 있음


import urllib.request
import urllib.parse

# 행정 안전부 RSS api
API = 'https://mois.go.kr/gpms/view/jsp/rss/rss.jsp'

params = []

for num in [1012, 1014, 1002, 1022]:
    params.append(dict(ctxCd=num))

print(params)

for c in params:
    param = urllib.parse.urlencode(c)

    url = API + '?' + param
    print(url)

    res = urllib.request.urlopen(url).read()
    print(res.decode('utf-8'))
