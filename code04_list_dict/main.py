num_list = [1,2,3,4,5]
#인덱싱 0부터 시작
print(num_list[0],num_list[-1])
#인덱싱 -는 뒤에서부터 시작

#in은 멤버쉽 연산자 
for i in num_list:
    print( i )

#슬라이싱(범위) 시작:끝 (끝을 비우면 끝까지)
print(num_list[0:3])
print(num_list[0:])

#1.리스트 추가
num_list.append(6)
num_list.append(7)
print(num_list[0:])


#2.리스트 삭제
del num_list[6]
print(num_list[0:])

del num_list[len(num_list) - 1]
print(num_list[0:])

#3. 리스트 수정
num_list[0] = 0
print(num_list[0:])

#4. 리스트 연산
test_list = [1,2,3]
sub_list = [4,5,6]
print(test_list + sub_list) #[1, 2, 3, 4, 5, 6]
print(test_list * 2) #[1, 2, 3, 1, 2, 3]


######################################

num_dic = {"m":"Moon", "s":"Seong", "ss":"Seong"}
print(num_dic["m"])

for k,v in num_dic.items():
    print(k,v)

for k in num_dic.keys():
    print(k)

for v in num_dic.values():
    print(v)

#추가
num_dic["j"] = "Jae"
print(num_dic["j"])

#제거
del num_dic["ss"]
print(num_dic)

#키에 없는 값 검색해도 에러없이 받기 결과값 : None
print(num_dic.get("k"))