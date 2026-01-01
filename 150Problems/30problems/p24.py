# find the given number is armstrong or not

def find_armstrong(num):
    temp_num=num
    temp=num
    length=len(f"{temp}")
    sumi=0
    while temp_num!=0:
        r=temp_num%10
        sumi+=(r**length)
        temp_num//=10
    if num==sumi:
        return True
    else:
        return False

number=int(input())
print(f"the given is number is Armstrong number or not:{find_armstrong(number)}")
