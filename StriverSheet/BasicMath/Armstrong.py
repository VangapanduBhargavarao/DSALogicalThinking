### check the given number is armstrong number or not
import math
def arm_strong(n):
    digits=math.floor(math.log10(n))+1
    temp=n
    sum=0
    while n!=0:
        digit=n%10
        sum=sum+(digit**digits)
        n//=10
    return True if temp==sum else False


n=int(input())
print(f"The give number is armstrong or not:{arm_strong(n)}")