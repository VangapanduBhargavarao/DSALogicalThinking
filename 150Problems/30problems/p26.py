### find the sum of the digits of the factorial of number
def fact(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    return fact
def find_sum(number:int)->int:
    sumi=0
    n=fact(number)
    while n!=0:
        r=n%10
        sumi+=r
        n//=10
    return sumi

num=int(input())
print(f"the sum for the given number is:{find_sum(num)}")

    