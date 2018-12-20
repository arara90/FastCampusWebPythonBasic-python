test = [1,2,3]

try :
  #print(test[3])
  print(test[2])
except:
    print("인덱스 에러 발생")
finally :
    print("fin")
  

test2 = 10
if(test2 == 10) : 
  raise Exception("test is 10")

  