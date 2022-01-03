import collections
import re
from typing import Deque

a=list(input())
b=[]
print(len(a))
for i in range(len(a)):
    if ord(a[i])>=65 :
        b.append(a[i])

for i in range(len(b)):
    if ord(b[i])<97:
        b[i]=chr(ord(b[i])+32)
c=list(reversed(b))
print(b)
print(c)
if b==c:
    print(True)
else:
    print(False)

#모범답안1
def isPalindrom(self,s:str)->bool:
    strs=[]
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs)>1:
        if strs.pop(0)!=strs.pop():
            return False
    return True
#모범답안2
def isPalindrom(self, s:str)->bool:
    strs: Deque=collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs)>1:
        if strs.popleft()!=strs.pop():
            return False
        return True
#모범답안3
def isPalindrom(self, s:str)->bool:
    s=s.lower()
    s=re.sub('[^a-z0-9]','',s)
    return s==s[::-1]