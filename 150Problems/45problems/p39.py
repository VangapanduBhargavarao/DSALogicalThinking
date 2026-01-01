### find the given number is perfect square or not

def find_perfect_square(num):
    low=1
    high=num
    while low<=high:
        mid=(low+high)//2
        if mid*mid==num:
            return mid
        elif mid*mid>num:
            high=mid-1
        else:
            low=mid+1


num=int(input())
print(f"the perfect square for given number is:{num} is :{find_perfect_square(num)}")