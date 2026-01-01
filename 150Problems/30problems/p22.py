## find the all the prime numbers between the give range is.
def isPrime(num):
    count_of_factors=0
    for i in range(1,num+1):
        if num%i==0:
            count_of_factors+=1
    if count_of_factors==2:
        return True
    else:
        return False
def list_of_primes(end):
    primes=[]
    for num in range(1,end):
        if isPrime(num):
            primes.append(num)
    return primes

end=int(input())
print(f"the  numbers of primes below the given range is :{list_of_primes(end)}")