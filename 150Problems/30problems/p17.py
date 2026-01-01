## find the armstrong numbers in the given range

first=int(input())
second=int(input())
result=[]
for number in range(first,second+1):
    temp=number
    n=len(f"{temp}")
    sumi=0
    temp_num=number
    while temp_num!=0:
        r=temp_num%10
        sumi=sumi+(r**n)
        temp_num//=10
    if sumi==temp:
        result.append(temp)
print(f"the fibonacci number is the range is :{result}")

