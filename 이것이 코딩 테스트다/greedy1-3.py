n=int(input())
s=list(map(int,input().split()))
s.sort()
result=0
cnt=0

for i in s:
    cnt+=1
    if cnt>=i:
        result+=1
        cnt=0

print(result)
    
