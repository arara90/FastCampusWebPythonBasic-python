

#내코드
print("================for=============")
a = [1, 5, 4, 3, 2]
print("시작 : " , a)
for i in range(1,len(a)):
    print("pivot index :" , i , "value :" , a[i])
    pivot=a[i] #pivot값 저장 
    for j in range(i,0,-1):
        if( pivot < a[j]):
            print(" swap[%d , %d]  " % ( pivot, a[j] ) )
            a[j+1] = a[j]
            a[j] = pivot  
            print("  >> ", a )     
print("끝 : ", a )

#while문으로
print("================while=============")
a = [1, 5, 4, 3, 2]
print("시작 : " , a)
for i in range(1,len(a)):
    pivot=a[i]
    j = i-1
    while j >= 0 :
        if (a[j] > pivot):
            a[j+1] = a[j]
            a[j] = pivot
        j = j-1
        
print("끝 : ", a )



#쌤코드
print("================teacher=============")
num_list = [1, 5, 4, 3, 2]
for i in range(1, len(num_list)):
    j = i - 1 # 삽입할 요소보다 앞의 인덱스
    key = num_list[i] # 삽입할 값 (=pivot)

    while num_list[j] > key and j >= 0: # 반복문 조건 비교
        num_list[j+1], j = num_list[j], j - 1 # 값을 대입
    num_list[j+1] = key # 요소 삽입

for i in num_list:
    print(i, end= ' ') # 1, 2, 3, 4, 5


