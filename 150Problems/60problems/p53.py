## print the fibonacii series for the numbers in recurisve function.
### this is the general approach write the recursive function approach
"""
def print_fib(n,a=0,b=1):
    while n!=0:
        print(a,end=" ")
        a,b=b,a+b
        n-=1
n=int(input())
print(f"The elements in the fibonacci:{print_fib(n)}")"""


#### Recursive function approach
def print_fib(n,a=0,b=1):
    if n!=0:
        print(a,end=" ")
        a,b=b,a+b
        print_fib(n-1,a,b)
n=int(input())
print_fib(n)
