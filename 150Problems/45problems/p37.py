## Happy number Checker.
# Here Happy number means the value is the square it's digit and add it to the sum if the value
# we obtain 1 then it is the happy number

def find_happy_number(num):
    seen=set()
    while num!=1 and num not in seen:
        seen.add(num)
        sumi=0
        while num!=0:
            sumi+=(num%10)**2
            num//=10
        num=sumi
    return num==1

number=int(input())
print(f"the given number is:{number} is Happy number or not:{find_happy_number(number)}")


