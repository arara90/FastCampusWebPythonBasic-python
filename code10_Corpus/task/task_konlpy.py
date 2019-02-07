from konlpy.tag import Okt
from random import randint 

NOUNS = ['한글', '한글날', '세종', '세종대왕', '패스트', '캠퍼스']
# 문자의 출현 빈도를 계산하기 위한 함수를 정의합니다.
def get_wc(content):
    ok = Okt() # Okt 객체를 함수 안에 선언했습니다.
    result = {} # 출현 빈도 계산을 위해 빈 딕셔너리를 선언합니다.
    for c in content: # 무작위로 문자열 결합된 값들을 하나씩 받아옵니다.
        temp = ok.pos(c) # Okt 객체의 메서드 중에서 pos 메서드를 이용해 (문자, 품사) 형태의 값을 리스트로 반환하여 temp 임시변수에 할당합니다.
        for t in temp: # 반환 받은 품사 리스트의 크기 만큼 반복합니다.
            if t[1] == 'Noun': # 품사가 명사인지 확인합니다.
                if not (t[0] in result): # 출현 빈도를 계산하기 위해 선언한 딕셔너리에 단어가 들어있는지 확인합니다.
                    result[t[0]] = 0 # 단어가 최초로 나왔다면, 0으로 초기화합니다.
                result[t[0]] += 1 # 찾은 단어의 값을 1 증가합니다.
    result = sorted(result.items(), key = lambda x:x[1], reverse = True) \
    # sorted 내장 함수를 이용해 딕셔너리를 내림 차순 정렬하고, 리스트로 반환합니다.
    print(result) # 출현 빈도를 출력합니다.

def get_rand():
    content = [] 
    for i in range(5): 
        temp = "" 
        j = 0 
        while j < 100: 
            temp += NOUNS[randint(0, 5)] 
            j += 1 
        content.append(temp) 
    #print(content)
    return content

# 단독 스크립트 실행인지 확인합니다.
if __name__ == "__main__":
    get_wc(get_rand()) # 단독 스크립트 실행이라면, 출현 빈도를 계산하는 함수를 실행합니다.
   #get_rand()