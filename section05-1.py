# beautiful Soup
# <메소드>
# find find_all
# select select_all

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse</title>
    </head>
    <body>
        <h1>FIRST</h1>
        <h2>SECOND</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there was thre little pigs.>
            <a href="http://example.com/1" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/2" class="sister" id="link2">Lacie</a>
            <a href="http://example.com/2" data-io="link3" class="brother" id="link2">Logun</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>
"""


# soup = BeautifulSoup(requests.get('http'))
soup = BeautifulSoup(html, 'html.parser')
# print(type(soup))
# print(soup.prettify()) # 내용 출력해줌


h1 = soup.html.body.h1
print(h1)

p1 = soup.html.body.p
print(p1)

p2 = p1.next_sibling.next_sibling
print(p2)

# 텍스트만 출력
# 접근자는 dir로 검색가능함
print(p1.string)
print(h1.string)
# print(dir(p2))

for v in p1.next_element:
    pass

# 1.
# 태그로 접근할 땐,
# find
link1 = soup.find_all('a', limit=1)
print(link1)

# id="link1" 아이디 조건
# string="title" 스트링 조건
# string=["Elsie"] 텍스트로 조건
link2 = soup.find_all('a', class_='sister')
print(link2)

for t in link2:
    print(t.string)

link3 = soup.find("a")
print(link3.string)

link4 = soup.find("a", {"class": "brother", "data-io": "link3"})
print(link4.string)


# 2.
# css 선택자를 쓸 때
# select

# '.'은 class 접근 의미함
link5 = soup.select_one('p.title > b')
print(link5)
print(link5.text)
print(link5.string)

# '#'은 id 의미함
link6 = soup.select_one('a#link1')
print(link6)

# [] 대괄호는 임의 속성값에 접근 가능함
link7 = soup.select_one("a[data-io='link3']")
print(link7)


link8 = soup.select('p.story > a')
print(link8) # 리스트니까 for 문 돌려야 string만 출력가능해
for i in link8:
    print(i.string)

link9 = soup.select('p.story > a:nth-of-type(2)')
print(link9)


link10 = soup.select('p.story')
for t in link10:
    temp = t.find_all('a')

    if temp:
        for v in temp:
            print('>>>>>', v.string)
    else:
        print('----', t.string)
