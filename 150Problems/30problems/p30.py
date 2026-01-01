### sum of the n natural numbers to find the values.
def find_sum(num):
    sumi=0
    for val in range(1,num+1):
        sumi+=val
    return sumi

num=int(input())
print(f"the given sum for n natural numbers:{find_sum(num)}")
