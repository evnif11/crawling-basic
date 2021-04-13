# urlopen 함수

import lxml
import urllib.request as req
from urllib.error import URLError, HTTPError


path_list = ['/Users/chanjoo/Documents/Python_Crawl/test1.jpg',
             '/Users/chanjoo/Documents/Python_Crawl/index.html']

target_url = ['https://pds.joins.com/news/component/htmlphoto_mmdata/202001/01/f86957cb-ee94-4611-bc81-a5478ca91f92.jpg',
              'http://www.google.co.kr']

for i, url in enumerate(target_url):
    try:
        response = req.urlopen(url)

        contents = response.read()

        print('------------------')
        print('Header Info- {} : \n{}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed")
        print("HTTPError Code :", e.code)
    except URLError as e:
        print("Download failed")
        print("URL Error Reason :", e.reason)
    else:
        print()
        print("Download Succeed")
