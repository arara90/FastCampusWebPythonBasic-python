import requests
from bs4 import BeautifulSoup as bs

URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="

def get_link():
    for page in range(1,11):
        req = requests.get(URL.format(str(page)))
        code = req.status_code
        if code == 200:
            soup = bs(req.text, 'html.parser')
            div = soup.find_all('div', attrs={'class':'list_con'})
            for data in div:
                a_tag=data.find('a', attrs={'title':'상세화면'})
                a_tag = a_tag.get_text() #콘텐츠만 문자열로 추출

                box_st1 = data.find('div', attrs={'class':'box_st1'})
                box_st1 = box_st1.get_text()

                print(a_tag.replace('\n','').replace('\t',''))
                print(box_st1)
                print('-----------------------------------')
        else:
            print('http error: ', code)
        

if __name__ == "__main__":
    get_link()

