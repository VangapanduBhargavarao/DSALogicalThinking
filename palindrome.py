def isPalindrome(x: int) -> bool:
        if x<0:
            return False
        temp=x
        reverse=0
        while temp!=0:
            digit=temp%10
            reverse=reverse*10+digit
            temp//=10
        return True if reverse==x else False
        
n=int(input())
print(f"The given number {n} is palindrome or not:{isPalindrome(n)}")