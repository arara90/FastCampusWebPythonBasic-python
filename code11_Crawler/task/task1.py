import requests
from bs4 import BeautifulSoup as bs
#http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page=2&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue=
# Paging작업 자동으로 이루어지게 할 것 이기때문에 page=2 부분은 page = {} 로 수정해서 URL에 저장 
URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="

def get_link():
    for page in range(1,11):
        req = requests.get(URL.format(str(page)))
        soup = bs(req.text,'html.parser')
        print(soup)

if __name__=="__main__":
    get_link()

## https://주소 > SSLError 발생
# get 메서드의 인자로 verify=False라는 것을 추가로 입력해야 합니다. (e.g., requests.get(URL.format(str(page)), verify=False)