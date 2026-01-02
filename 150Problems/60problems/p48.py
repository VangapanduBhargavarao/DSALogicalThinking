#### count the repeated number more times 
nums=list(map(int,input().split()))
appears=[]
seen=dict()
for val in nums:
    seen[val]=seen.get(val,0)+1
for key,val in seen.items():
    if val>=2:
        appears.append(key)
print(f"The elements that are the repeated more than twices are:{appears}")
