
from lxml.html import tostring, fromstring
import requests


def main():
    # 세션
    session = requests.Session()
    # 크롤링 대상 URL
    response = session.get("https://www.naver.com")
    # 신문 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 타입으로 출력
    print(urls)

    # 결과 출력
    for name, url in urls.items():
        print(name, url)


def scrape_news_list_page(response):
    urls = {}

    root = fromstring(response.content)

    for a in root.xpath('//div[@class="thumb_area"]/div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]'):

        name, url = extract_contents(a)
        urls[name] = url

        # print(tostring(a, pretty_print=True))

    return urls


def extract_contents(dom):
    link = dom.xpath("./div/a")[2].get('href')
    name = dom.xpath("./a/img")[0].get('alt')

    return name, link

if __name__ == "__main__":
    main()
