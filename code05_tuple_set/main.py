
#tuple
num_tuple = (1,2,3)
print(num_tuple)

#다음은 에러
#num_tuplep[0] = 0
# del num_tuple[0]

#set (중복제거)
num_set = {1,1,2,2,3}
print(num_set)
#결과 : {1, 2, 3}

# 1.set 추가
num_set.add(4)
print(num_set)

# 2.set 집합연산
set1 = {1,1,2,2,3}
set2 = {1,1,2,2,4}
print(set1 & set2) #여집합  {1, 2}
print(set1 | set2) #합집합  {1, 2, 3, 4}
print(set1 - set2) #차집합  {3}


# cf) 리스트 연산
# test_list = [1,2,3]
# sub_list = [4,5,6]
# print(test_list + sub_list) #[1, 2, 3, 4, 5, 6]
# print(test_list * 2) #[1, 2, 3, 1, 2, 3]

# 3.생성자 이용해서 타입 변경 : list(), dict(), set(), tuple()
test_list = [1,2,3,1,2,3]
test = set(test_list)
print(test) #{1, 2, 3}
#print(test[0]) #TypeError: 'set' object does not support indexing
