
num_list = [1,2,3,4,5]
double_list = [num_list,num_list]

#1
print("#1")
for num in num_list:
    print(num, end = '!')

#2
print("\n#2")
for i in double_list:
    for j in num_list:
        print(j,end = '-')

#3
print("\n#3")
for i in double_list:
    for j in i:
        print(j,end = '-')

#4 : 추가
print("\n#4")
num_list[len(num_list) - 1] = 6
print(num_list)

#5 
print("\n#5")
num_list = num_list + num_list 
print(num_list) # [1, 2, 3, 4, 6, 1, 2, 3, 4, 6]
num_list = num_list * 2 
print(num_list) # [1, 2, 3, 4, 6, 1, 2, 3, 4, 6, 1, 2, 3, 4, 6, 1, 2, 3, 4, 6]

#6
print("\n#6")
double_list[1] = []
print(double_list) #[1, 2, 3, 4, 5, []]


#7 리스트 슬라이싱
a = [1, 2, 3, 4]
print("\n#7 리스트 슬라이싱")
print(a[:]) # 1, 2, 3, 4 (0~끝)
print(a[0:]) # 1, 2, 3, 4 (0~끝)
print(a[:1]) # 1 (0~(1-1))
print(a[1:3]) # 2, 3 (1~(3-1))
print(a[:-1]) # 1, 2, 3 (0~(1-(-1)))

print(a.index())