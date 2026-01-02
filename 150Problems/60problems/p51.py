### add the all digits sum until the number will come to single digitt

num=int(input())
while num>10:
    sumi=0
    while num!=0:
        sumi+=(num%10)
        num//=10
    num=sumi

print(f"after perform the operations the values are {num}")