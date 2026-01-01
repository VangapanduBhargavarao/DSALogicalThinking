## find the largest palindrome in the given string
## here we follow the approach first find the substrigns and after that find valid palindorm or not
def isValid(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
def find_valid_palindrome(s):
    max_length=0
    length=len(s)
    for i in range(length):
        for  j in range(i,length):
            string=s[i:j+1]
            if isValid(string):
                if len(string)>max_length:
                    max_length=len(string)
    return max_length

string=input()
print(f"the maximum length of substring is:{find_valid_palindrome(string)}")


### for the above problem is there anything we can optimze into the normal solution
def isValid(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True


