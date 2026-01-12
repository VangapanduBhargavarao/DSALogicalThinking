####  write the Recursive program to sum of the first n numbers

def sumi(n):
    if n==1:
        return 1
    return n+sumi(n-1)

N=int(input())
print(f"The sum of {N} numbers is:{sumi(N)}")