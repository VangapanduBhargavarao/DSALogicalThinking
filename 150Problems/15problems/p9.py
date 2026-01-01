# calculate the Nth fibonacci series.
"""def number(n:int)->int:
    sumi=0
    a,b=0,1
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    else:
        for _ in range(1,n):
            a,b=b,a+b
        return b
            
    return sumi
n=int(input())
print(f"Fibonacci number upto {n} terms is:{number(n)}")
"""

### in the recurisve approach

def Recursive(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 1
    else:
        return Recursive(n-1)+Recursive(n-2)
n=int(input())
print(f"{Recursive(n)}")