###################Request###################
# 웹자원 요청하는 패키지
###############################################
import requests

#1.get
params = {'key1':1, 'key2':2}
r = requests.get('https://www.fastcampus.co.kr/dev_online_introdev/', params=params) #http get 요청

print(r.encoding) #utf-8
print(r.url) #https://www.fastcampus.co.kr/dev_online_introdev?key1=1&key2=2
print(r.text) #응답받은 콘텐츠를 해석할 수 있는 인코딩 형태로 만들어줍니다.


#2.post
data = {'key1':1, 'key2':2}
r = requests.get('https://www.fastcampus.co.kr/dev_online_introdev/', data=data)

#3.Header정보
#F12 -> Network > request Header > User-agent에서 기기정보/브라우저정보가져오기
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'}
r = requests.get('https://www.fastcampus.co.kr/dev_online_introdev/', headers=headers)

