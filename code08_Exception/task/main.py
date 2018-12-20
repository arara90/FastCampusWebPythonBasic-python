
##예제1
def sum():
    i = 0
    try:
        # 1번 코드, 예외 발생 가능성이 있는 코드 구문
        while i < 100:
            i += 1
    except:
        # 2번 코드, 예외 발생시 실행되는 코드 구문
        i = 0
    return i

print(sum()) # 100


##예제2
class cat :
    def __init__(self,name):
        if not name :
            "이름이 필요합니다!"        
cat1 = cat("hi")
#cat2 = cat() 에러

try:
        cat2 = cat()
except:
        print("에러")
finally:
        print("완료")


#예제3
try:
    i + 1 # NameError
    '1' + 1  # TypeError
except TypeError:
    print('Type Error')
except NameError:
    print('Name Error')


# Name Error 출력
# i+1 이 먼저 오류 발생

#예제4 - 복수개의 예외처리를 튜플로 전달
try:
    j + 1 # NameError
    '1' + 1  # TypeError
except (TypeError, NameError):
    print('Type Error or Name Error')

#예제 5 : Exception - Exception(클래스) 키워드를 사용하면 프로그램이 종료되지 않고 예외 이유를 알 수 있음
# 키워드 사용안하면 종료하고 어떤 예외에 의해 종료되었는지 확인
try:
    y + 1
except Exception as e:
    print(e) # name 'y' is not defined

#예제6 : finally
try:
     1 / 0
     print("hihi2")
except Exception as e:
    print(e) 
finally:
    print('run finally') 
print("hihi2")
#fun finally, hihi2만 출력

print('#####################')
#예제 7 : finally 2
try:
    1 / 0 # 1번 코드
except Exception as e:
    print(e) # 2번  코드
    1 / 0  # 4번 코드
finally:
    print('run finally') # 3번 코드

# division by zero-> run finally -> division by zero
# 보통 오류의 유무와 상관없이 실행 코드 종료시 finally에 외부자원 반납하게 함
