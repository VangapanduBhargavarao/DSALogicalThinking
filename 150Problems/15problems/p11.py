### find the LCM of the given number
n1=int(input())
n2=int(input())
if n1>n2:
    n1,n2=n2,n1
factor=n1
while factor:
    if n1%factor==0 and n2%factor==0:
        break
    factor-=1
result=(n1*n2)//(factor)
print(f"the LCM of two numbers is:{result}")