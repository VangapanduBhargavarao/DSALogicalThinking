# factorial of a number

N=int(input())
fact=1
for i in range(1,N+1):
    fact*=i
print(f"Factorial of number is:{fact}")