### find the reverse of the given number
class Negative(Exception):
    pass

def Reverse(n:int)->int:
    reverse=0
    while n!=0:
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
    return reverse

try:
    n=int(input("enter"))
    if n<0:
        raise Negative

except ValueError:
    print("Enter the correct value")
else:
    print(f"The Reverse of given number is :{Reverse(n)}")