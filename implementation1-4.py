a=list(input())
b=[0]*len(a)
c=[0]*len(a)
j=0
h=0
cnt=0
result=0
for i in range(0,len(a)):
    if ord(a[i])<=57:
        b[j]=a[i]
        j+=1
        cnt+=1
    else:
        c[h]=a[i]
        h+=1
for i in range(0,cnt):
    result+=int(b[i])
    c.remove(0)

c.sort()
strA=''.join(c)
print(strA,end='')
print(result)
