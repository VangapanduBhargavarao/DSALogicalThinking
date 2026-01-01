## break the number into the suare the digits
def sumi_square(num):
    sumi=0
    while num!=0:
        r=num%10
        sumi+=(r**2)
        num//=10
    return sumi
num=int(input())
print(f"the values of the given number is:{sumi_square(num)}")
