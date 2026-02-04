###### In the below problem we have to find the pascals triange in the given order.

def funcncr(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res

n=int(input("enter the row"))
r=int(input("enter col"))
print(f"value is:{funcncr(n-1,r-1)}")