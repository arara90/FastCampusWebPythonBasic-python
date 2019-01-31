from konlpy.tag import Okt
from random import randint

NOUNS = ['한글', '한글날', '세종', '세종대왕', '패스트', '캠퍼스']

def get_wc(content) :
    #print(content)
    ok = Okt()
    result = {} #Dic
    #result = ok.pos(content[1]) 
    #pos는 문자열을 (문자,품사)로 분해해서 리스트 형태로 반환

    for c in content:
        tmplist = ok.pos(c)
        for i in tmplist:
            if i[1] == "Noun" :
                if i[0] not in result: # result = result.keys() , test의 test1.py 참고
                    result[i[0]] = 0
                result[i[0]] += 1
    result = sorted(result.items(), key = lambda x:x[1], reverse=True)
    print(result)


def get_rand():
    content = [] #List
    
    for i in range(5):
        temp = ""
        j=0
        while j < 100:
            temp += NOUNS[randint(0,5)]
            j+=1
        content.append(temp)
    return(content)


if __name__ == "__main__":
        get_wc(get_rand())