#### in the given number count the number of digits we have
class NegativeError(Exception):
    print("Enter the positive number")

def count_digits(n:int)->int:
    count=0
    while n!=0:
        count+=1
        n//=10
    return count


try:
    n=int(input("enter:"))
    if n<0:
        raise NegativeError
except ValueError:
    print("enter the correct")
else:
    print(f"The number of digits in number is:{count_digits(n)}")