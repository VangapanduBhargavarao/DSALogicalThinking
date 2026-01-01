## perfect number validator
def perfect(n):
    sumi=0
    for i in range(1,n):
        if n%i==0:
            sumi+=i
    if sumi==n:
        return True
    else:
        return False

number=int(input())
print(f"the  number :{number} is perfect or not:{perfect(number)}")