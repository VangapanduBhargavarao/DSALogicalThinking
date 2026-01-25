#### this problem is used to buy the stok on the last day and try to make profit.
### this one is the some problem in the modify the values in the given code and how it works.

def stock_buy(nums):
    n=len(nums)
    maxprofit=float('-inf')
    minbuy=nums[0]
    for i in range(n):
        maxprofit=max(maxprofit,nums[i]-minbuy)
        minbuy=min(minbuy,nums[i])
    return maxprofit if maxprofit!=float('-inf') else 0


nums=list(map(int,input().split()))
print(f"for given value the maxprofit is:{stock_buy(nums)}")
