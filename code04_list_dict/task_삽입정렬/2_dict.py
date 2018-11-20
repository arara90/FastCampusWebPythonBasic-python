a = {"a":1, "b":2, "c":3}
a["a"] = 0 # 수정
a["d"] = 4 # 추가
del a["a"] # 삭제
print("\n#1")
print(a) # {'b': 2, 'c': 3, 'd': 4}

for key in a:
  print(a[key], end = ' ') # 2 3 4

#Method
del a["d"] # 삭제
a["a"] = 1 # 추가
print("\n#2")
print(a)

# keys
print("\n#3 key")
for k in a.keys():
    print(k, end=' ') # a b c

# values
print("\n#4 value")
for v in a.values():
    print(v, end=' ') # 1 2 3

# items
print("\n#5 items")
for k, v in a.items():
    print(k, v, end = ' ') # a1 b2 c3


# 생성자
print("\n\n#6 생성자")

a = [[1, 2], [3, 4], [5, 6]]
b = {"a":1, "b":2, "c":3}

print(list(b.keys())) # ['a', 'b', 'c']
print(list(b.values())) # [1, 2, 3]
print(list(b.items())) # [('a', 1), ('b', 2), ('c', 3)]
# 만약 a = [1,2,3,4,5] 형태였다면 TypeError
print(dict(a)) # {1: 2, 3: 4, 5: 6}