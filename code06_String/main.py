################스트링##############
test1 = "Life is too short, %s"
result1 = test1 % "You need python."
print(result1)


test2 = "Life is too short, %s %s %s"
result2 = test2 % ("You", "need", "python.")
print(result2)

################정수##############
test3 = "Life is too short,  %d"
result3 = test3 % 10
print(result3)

#result3_1 = test3 % "10"
#print(result3_1) #TypeError: %d format: a number is required, not str (예외 %s는 받을 수 있음)


################실수##############
test4 = "Life is too short,  %.2f" #두자리 소수점까지 표현하라
result4 = test4 % 100
print(result4) #Life is too short,  100.00

result4_1 = test4 % 100.1234
print(result4_1) #Life is too short,  100.12

################format 함수 이용##############
test5 = "Life is too short, {} {} {}"
result5 = test5.format("You", "need", 10)
print(result5) #Life is too short, You need 10 : 정수형도 잘 출력

################ESCAPE 문자 ##############
test6 = "\'Life is too short,\n You need python\'"
print(test6) 