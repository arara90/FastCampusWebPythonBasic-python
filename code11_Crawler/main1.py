import requests
from bs4 import BeautifulSoup as bs4

URL="https://www.fastcampus.co.kr/dev_online_introdev/#row_course"

rq = requests.get(URL)
soup = bs4(rq.content, 'html.parser')
print(soup)