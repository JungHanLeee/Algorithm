n=list(map(int,input()))
out=[]
p=1
for i in range(len(n)):
    out.append(p)
    p=p*n[i]
p=1
for i in range(len(n)-1,0-1,-1):
    out[i]=out[i]*p
    p=p*n[i]
print(out)