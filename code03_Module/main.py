# 모듈1.기본
#import sub
#print(sub.sum(1,1))

# 모듈2.from 사용
#from sub import sum
#print(sum(1,2))

# 모듈3.별칭
#from sub import sum as s
#print(s(1,2))

###############################################3

#패키지1.기본
#from package import pck
#print(pck.sum(1,1))

# 패키지2. 별칭
from package import pck as p
print(p.sum(1,2))

