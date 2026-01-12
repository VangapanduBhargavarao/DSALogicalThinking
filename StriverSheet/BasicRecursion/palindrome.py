#### check the given string is the palindrome or not

### Before going to Recursive manner we will move to the two pointers approach

"""
def isPalindrome(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

s=input()
print(f"The given string :{s} is palindrome or not:{isPalindrome(s)}")"""




#### is this any way we can do with the help of the Recusrion 
def isPalindrome(i,s):
    if i>=len(s)//2:
        return True
    if s[i]!=s[len(s)-i-1]:
        return False
    return isPalindrome(i+1,s)


s=input()
print(f"The given string is palindrome or not:{isPalindrome(0,s)}")