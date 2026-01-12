#### write the recusrive function to factorial of number

def fact(N):
    if N==1 or N==0:
        return 1
    return N*fact(N-1)

N=int(input())
print(f"The factorial of Number :{N} is :{fact(N)}")