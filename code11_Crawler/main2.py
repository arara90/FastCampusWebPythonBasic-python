import requests
from bs4 import BeautifulSoup as bs

#크롬에서 태그 선택 오른쪽 > copy > copy selector
#https://www.fastcampus.co.kr/dev_online_introp/#text-block-17
URL = "https://www.fastcampus.co.kr/dev_online_introp"

rq = requests.get(URL)
soup = bs(rq.content,'html.parser') 

#print(soup)
#여러가지 find는 보통 상위태그 가져올때 
# (class, id, .. ) attr={key:value,...} 

# div.vc_toggle_content > ul > li
#find는 BeautifulSoup 객체를 반환하고, find_all, select는 결과를 BeautifulSoup 객체 List로 반환한다
li_list = soup.find_all('div', class_ = 'vc_toggle_content')

for li in li_list:
    print(li)


#for li in li_list:
#   ul = li.select('ul > li')
#   for l in ul:
#       print(l.get_text())
   



