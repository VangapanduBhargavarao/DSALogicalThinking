### find the harshad number
def harshad_or_not(num):
    temp=num
    sumi=0
    while temp:
        sumi+=(temp%10)
        temp//=10
    if num%sumi==0:
        return True
    else:
        return False
number=int(input())
print(f"The given number {number} is Harshad number or not:{harshad_or_not(number)}")