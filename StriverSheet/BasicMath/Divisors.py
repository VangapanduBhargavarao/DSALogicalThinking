### Find the total divisors of the given number
"""
def total_divisors(num):
    result=[]
    for factor in range(1,num+1):
        if num%factor==0:
            result.append(factor)
    return result

num=int(input("Enter the number"))
print(f"the total divisors for given number is:{total_divisors(num)}")"""




#### find the optimal approach for the above problem
## here we have to trim down the iteration upto the square root of the n.
## so generally if d is divisor of n then n/d is also is a divisor for the problem.
import math
def total_divisors(num):
    result=[]
    for i in range(1,math.isqrt(num)+1):
        if num%i==0:
            result.append(i)
            if i!=num//i:
                result.append(num//i)
    return result

num=int(input())
print(f"the divisors for given number is :{total_divisors(num)}")
