# reverse the string
"""
def reverse(s:str)->str:

    n=len(s)
    left,right=0,n-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
s=input()
print(f"the Reverse string for given string {s} is :{reverse(s)}")
"""

def reverse(s:str)-> str:
    return s[::-1]
s=input()
print(f"The reverse for given string is:{reverse(s)}")