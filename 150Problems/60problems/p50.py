### given range find the prime numbers and find the sum of those prime numbers.

start=int(input())
end=int(input())
def isPrime(num):
    count_of_factors=0
    for i in range(1,num+1):
        if num%i==0:
            count_of_factors+=1
    if count_of_factors==2:
        return True
    else:
        return False

sumi=0
for i in range(start,end+1):
    if isPrime(i):
        sumi+=i
print(f"the sum of prime numbers in the give range is :{sumi}")
