# selenium 실습예제 2

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 브라우저 실행 없는 'headless' 모드
chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정
browser = webdriver.Chrome('./webdriver/chromedriver', options=chrome_options)
# browser = webdriver.Chrome('./webdriver/chromedriver')

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

# bs 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup.prettify())

# 메인 상품리스트
product_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')
# print(product_list)

for v in product_list:

    if not v.find('div', class_='ad_header'):

        print(v.select('p.prod_name > a')[0].text.strip())
        print(v.select('div.thumb_image > a > img')[0]['src'])
        print(v.select('p.price_sect > a')[0].text.strip())

    print()
