def sum(x,y, test = 1) :
    return x+y+test

x=1
y=1
print(sum(x,y))   #3
print(sum(x,y,3)) #5  

##이름있는 인자##
def sum(x, y, z = 5):
    return x + y + z

print(sum(x = 10, y = 10, z = 10)) # 30 
print(sum(y = 10, x = 10)) # 25
print(sum(z = 10, y = 10, x = 10)) # 30


############가변길이#############

def sum1(x,*y) :
    #sum_list = []
    result = 0
    for i in y : 
        #sum_list.append(i)
        result += i
    #print(sum_list)
    print(x+result)
sum1(1,1,2,3,4,5) #16


#########가변길이 인자 순서############
def sum( *number,fl):
  sum = 0
  for i in number:
    sum += i
  return sum + fl

print(sum(1, 2, 3, 4, 5, fl = 1.0)) # 16.0
#print(sum(fl = 1.0, 1, 2, 3, 4, 5)) # SyntaxError 에러 발생!

##############################3

def sum2(one,two) :
    return one+two

print(sum2(one=1,two=1))

###########################



def sum3(a,b) : return a+b
def multiply(a,b) : return a*b

func = [sum3,multiply]
print(func[0](1,2) , func[1](1,2))  #3,2



