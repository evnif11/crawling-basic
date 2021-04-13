# section02-1
# urllib 사용법 및 기본 스크랩핑


import urllib.request as req

# 파일 URL
img_url = ('http://newsimg.hankookilbo.com/cms/articlerelease/'
           '2019/04/29/201904291390027161_3.jpg')
html_url = 'http://www.google.co.kr'

# 다운 받을 경로
save_path1 = '/Users/chanjoo/Documents/Python_Crawl/test1.jpg'
save_path2 = '/Users/chanjoo/Documents/Python_Crawl/index.html'


# 예외처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    print(header1)
    print(header2)

    print('filename1 {}'.format(file1))
    print('filename2 {}'.format(file2))
