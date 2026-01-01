## find the divisors of the number
def divisiors(num):
    divisiors=[]
    for i in range(1,num+1):
        if num%i==0:
            divisiors.append(i)
    return divisiors

num=int(input())
print(f"the number of divisors for number is :{divisiors(num)}")