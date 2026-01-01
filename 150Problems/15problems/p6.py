## gcd of a two numbers.

n1=int(input())
n2=int(input())
if n1>n2:
    n1,n2=n2,n1
factor=n1
while n1!=0:
    if n1%factor==0 and n2%factor==0:
        print(f"The Gcd of {n1} and {n2} is :{factor}")
        break
    factor-=1
