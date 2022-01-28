import sys

n=list(map(int,input()))
max_n=0
min_n=sys.maxsize

for i in n:
    min_n=min(min_n,i)
    max_n=max(max_n,i-min_n)
print(max_n)
