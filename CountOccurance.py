'''
If we want to count occurance of word
sting.count(substring)
'''

s=input("Enter String:")
b=input("What to find:")
a=1
results=0
for i in range(len(s)):
    if s[i:i+len(b)] == b:
        results += 1
print(results)
