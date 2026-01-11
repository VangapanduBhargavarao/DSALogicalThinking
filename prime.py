### check for the given number is prime or not
"""
def isPrime(num):
    count_of_factors=0
    for factor in range(1,num+1):
        if num%factor==0:
            count_of_factors+=1
    return True if count_of_factors==2 else False

num=int(input())
print(f"the given number {num} is Prime or not:{isPrime(num)}")"""



### optimal appriach for the above prime number then we can simply find the value of the prime number
import math
def isPrime(num):
    count=0
    for factor in range(2,math.isqrt(num)+1):
        if num%factor==0:
            count+=1
    return True if count==0 else False

num=int(input())
print(f"The number {num} is prime number or not:{isPrime(num)}")