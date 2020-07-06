from fractions import Fraction
def nextseq(val):
    """수열의 다음항을 반환하는 함수"""
    return 1+1/(1+val)

mylist, myresult =[Fraction(3,2)],[]

for i in range(0,999):
    value = nextseq(mylist[i])
    mylist.append(value)
    if len(str(value.numerator))>len(str(value.denominator)):
        myresult.append(value)
        
print(len(myresult))
# print(len(mylist))
# 153