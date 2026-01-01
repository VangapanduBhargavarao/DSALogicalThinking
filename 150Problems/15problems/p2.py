# check the whether given number is prime or not

n=int(input())
count_factors=0
for i in range(1,n+1):
    if n%i==0:
        count_factors+=1
if count_factors==2:
    print("given number is prime number")
else:
    print("given number is not prime number")