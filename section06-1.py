# selenium 패키지 사용
# 기본 브라우저만 렌더링 된 후 자바스크립트가 실행되며 ajax로 가져옴
# 동적 렌더링된 페이지 크롤링 하는 법


from selenium import webdriver

# 변수 초기화, 경로설정
browser = webdriver.Chrome('./webdriver/chromedriver')

# 크롬 브라우저 내부 대기 (사양을 고려해야함)
browser.implicitly_wait(5)

# print(dir(browser))


# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용보기
print(browser.page_source)
print(browser.session_id)
print(browser.title)
print(browser.current_url)
print(browser.get_cookies())


# 검색창 input 선택
element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

# 검색어 입력
element.send_keys('환율')
element.submit()

# 스크린샷 저장
browser.save_screenshot('/Users/chanjoo/Documents/Python_Crawl/screenshot/1.jpg')
browser.get_screenshot_as_file('/Users/chanjoo/Documents/Python_Crawl/screenshot/2.jpg')

browser.quit()
