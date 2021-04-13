# selenium 실습예제 + 추가 기능

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib import request
import xlsxwriter

# 이미지 바이트 처리
from io import BytesIO

# 엑셀 처리
workbook = xlsxwriter.Workbook('Users/chanjoo/Documents/Python_Crawl/crawling_list')

# 워크 시트
worksheet = workbook.add_worksheet()

# 브라우저 실행 없는 'headless' 모드
chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정
# browser = webdriver.Chrome('./webdriver/chromedriver', options=chrome_options)
browser = webdriver.Chrome('./webdriver/chromedriver')

# 브라우저 내부 대기
browser.implicitly_wait(2)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 시작 페이지
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 더보기 클릭
# 1. Explicitly wait(자주 쓰임) : 실제 나타나면 바로 실행
WebDriverWait(browser, 3).until(ec.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 2. Implicitly wait
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 체크박스 클릭
WebDriverWait(browser, 3).until(ec.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[13]/label'))).click()

# 중간 확인
# print(browser.page_source)
time.sleep(3)

# 시작 페이지 , 끝 페이지
cur_page = 1
target = 5

# 엑셀 숫자
cnt = 1

while cur_page <= target:


    # bs 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # print(soup.prettify())

    # 메인 상품리스트
    product_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')
    # print(product_list)
    print('***** current paget {}'.format(cur_page), '*****')
    for v in product_list:

        if not v.find('div', class_='ad_header'):

            prod_name = v.select('p.prod_name > a')[0].text.strip()
            prod_price = v.select('p.price_sect > a')[0].text.strip()
            # img = 'http:' + v.select('div.thumb_image > a > img')[0]['src']
            # img_data = BytesIO(request.urlopen(img).read())

            # 엑셀 저장
            worksheet.write('A%s'%cnt, prod_name)
            worksheet.write('B%s'%cnt, prod_price)
            # worksheet.insert_image('C%s'%cnt, prod_name, {'image_data': img_data})

            cnt += 1

        print()
    print()

    # 페이지 증가
    cur_page += 1

    # 페이지 이동 클릭
    WebDriverWait(browser, 2).until(ec.presence_of_element_located((By.CSS_SELECTOR,'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()

    # 대기
    time.sleep(3)





browser.close()
workbook.close()
