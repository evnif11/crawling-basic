# lxml 사용 기초 스크랩핑
# pip install lxml, requests, cssselect

import lxml.html
import requests


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    response = requests.get("https://www.naver.com")
    urls = scrape_news_list_page(response)

    # 결과 출력
    for url in urls:
        print(url)


def scrape_news_list_page(response):
    urls = []

    root = lxml.html.fromstring(response.content)
    for a in root.cssselect('._NM_NEWSSTAND_THUMB a.btn_popup'):

        url = a.get('href')
        if url == '#':
            continue
        urls.append(url)

    return urls


if __name__ == "__main__":
    main()
