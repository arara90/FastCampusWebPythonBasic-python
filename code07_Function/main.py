def sum(x,y, test = 1) :
    return x+y+test

x=1
y=1
print(sum(x,y))   #3
print(sum(x,y,3)) #5  

#########################

def sum1(x,*y) :
    #sum_list = []
    result = 0
    for i in y : 
        #sum_list.append(i)
        result += i
    #print(sum_list)
    print(x+result)

sum1(1,1,2,3,4,5) #16

##############################3

def sum2(one,two) :
    return one+two

print(sum2(one=1,two=1))