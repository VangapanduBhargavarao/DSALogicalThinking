### finding the prime numbers between the given range.
def isPrime(n):
    count_of_factors=0
    for i in range(1,n+1):
        if n%i==0:
            count_of_factors+=1
    if count_of_factors==2:
        return True
    else:
        return False
def prime_numbers(start,end):
    result=[]
    for i in range(start,end+1):
        if isPrime(i):
            result.append(i)
    return result        
start=int(input())
end=int(input())
print(f"the prime numbers between the given range is :{prime_numbers(start,end)}")