# 이미지 데이터 수집하기

import os
from urllib import parse, request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 헤더 정보 초기화, 페이크 유저 정보, 헤더 삽입
opener = request.build_opener()
opener.addheaders = [('User-agent', UserAgent().ie)]
request.install_opener(opener)

# 네이버 검색 url 생성하기
base = 'http://www.ssg.com/search.ssg?target=all&query='
quote = parse.quote_plus('바나나')
url = base + quote

print(url)

res = request.urlopen(url)


# 이미지 저장 경로
savePath = '/Users/chanjoo/Documents/Python_Crawl/images/'

# 폴더 생성 예외 처리
try:
    # 폴더 없으면 생성하기
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError:
    print('폴더 생성 실패')
    print(OSError.filename)
    raise RuntimeError('system exit')

else:
    # 폴더 생성됐거나 존재함
    print('폴더 생성됨')


soup = BeautifulSoup(res, "html.parser")
# print(soup.prettify())

img_list = soup.select('div.cunit_prod > div.thmb > a.clickable > img')

# find 메소드로 !
# img_list2 = soup.find_all("a", class_="clickable")

# for v in img_list2:
#     img_t = v.find('img')
#     print(img_t.attrs['src'])


print(img_list)

for i, img in enumerate(img_list, 1):
    if i > 20:
        break

    src = img['src']
    print()
    print()
    print()
    print(src, i)

    # 저장 파일 이름 지정해주기
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
    print(fullFileName)

    # / 지워주기

    # 1. //를 지운다
    # src = src[2:]

    # 2. 왼쪽에 있는 /를 모두 지운다
    #    ///asdasd -> asdasd
    #    //foo -> foo
    # src = src.lstrip('/')

    # 3. http를 붙인다
    # src = 'http:' + src

    # 4. 정규화한다.
    if src.startswith('//'):
        src = 'http:' + src

    # 다운로드
    request.urlretrieve(src, fullFileName)

print('다운로드 완료')
