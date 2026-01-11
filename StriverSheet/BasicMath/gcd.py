### for given two numbers find the greatest common divisor.
"""
Docstring for gcd



def find_greatest(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    factor=n1
    while factor!=0:
        if n1%factor==0 and n2%factor==0:
            return factor
        factor-=1

num1=int(input())
num2=int(input())
print(f"the gcd for two numbers:{num1} and {num2} is:{find_greatest(num1,num2)}")"""

### the above approach was the good but we have to find the optimal approach.


### optimal approach to gcd.
def find_gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a


num1=int(input())
num2=int(input())
print(f"gcd for two numbers {num1} and{num2} is:{find_gcd(num1,num2)} ")
        