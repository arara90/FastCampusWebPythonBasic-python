# 1번 코드
from time import time

# 2번 코드
def run_time(f):
    # 시작 시간
    start = time()
    f #sum 함수 실행
    str = "실행시간 %t" 
    print( str % (time() - start))  # 종료 시간 - 시작 시간(총 수행 시간)을 계산하여 정수 값으로 출력합니다.

# 3번 코드
def sum():
    sum = 0
    while sum < 100:
        sum += 1
        print(sum) # 1 2 3 ... 100

# 4번 코드
run_time(sum()) # 30 
