#### find the give number is perfect number or not

def perfect_number(num):
    sum=0
    for factor in range(1,num):
        if num%factor==0:
            sum+=factor
    return True if sum==num else False



num=int(input())
print(f"the given number is perfect number or not:{perfect_number(num)}")

