def Insertion() :
    num_list = [1, 5, 4, 3, 2]
    for i in range(1, len(num_list)):
        j = i - 1 # 삽입할 요소보다 앞의 인덱스
        key = num_list[i] # 삽입할 값 (=pivot)

        while num_list[j] > key and j >= 0: # 반복문 조건 비교
            num_list[j+1], j = num_list[j], j - 1 # 값을 대입
        num_list[j+1] = key # 요소 삽입

    for i in num_list:
        print(i, end= ' ') # 1, 2, 3, 4, 5


Insertion()
