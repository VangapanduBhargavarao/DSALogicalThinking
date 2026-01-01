# count vowels and consonants
s=input()
vowel=consonant=0
vowels={'a','e','i','o','u'}
for ch in s:
    if ord(ch)>=97 and ord(ch)<=122:
        if ch in vowels:
            vowel+=1
        else:
            consonant+=1
print(f"{s} contains {vowel} vowles and {consonant} consonants")
       
