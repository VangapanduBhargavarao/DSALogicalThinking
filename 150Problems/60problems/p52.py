### find the sum of the prime factors for that number.
def isPrime(num):
    count_of_factors=0
    for i in range(1,num+1):
        if num%i==0:
            count_of_factors+=1
    if count_of_factors==2:
        return True
    else:
        return False
number=int(input())
sumi=0
for i in range(1,number+1):
    if number%i==0:
        if isPrime(i):
            sumi+=i
print(f"the sum of prime facotrs are:{sumi}")