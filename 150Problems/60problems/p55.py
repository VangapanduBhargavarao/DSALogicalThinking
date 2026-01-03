### Longest substring without repeating the characters.
def longest_substring(s:str)->str:
    n=len(s)
    left=max_length=right=first_postion=last_position=0
    seen=set()
    while right<n:
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        length=right-left+1
        if length>max_length:
            max_length=length
            first_postion=left
            last_position=right
        seen.add(s[right])
        right+=1

    return s[first_postion:last_position+1]

string=input()
print(f"The longest substring in the current string is:{longest_substring(string)}")