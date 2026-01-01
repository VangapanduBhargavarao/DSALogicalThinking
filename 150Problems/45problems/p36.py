def find_count(n):
    count=0
    while n!=1:
        if n%2==0:
            n//=2
        else:
            n=(n*3)+1
        count+=1
    return count

number=int(input())
print(f"The number of steps is :{find_count(number)}")