n=int(input())
move=list(input().split())
k=len(move)
left=0
right=0

arr=[[0 for x in range(n)]for y in range(n)]
for z in range(0,n):
    for q in range(0,n):
        arr[z][q]="0"
for i in move:
    while(k>0):
        if i=='R':
            right+=1
            arr[left][right]="1"
            if right>n:
               k+=1
               continue
            else:
                arr[left][right-1]="0"
        elif move[i]=='L':
            right-=1
            arr[left][right]="1"
            arr[left]
            if right<0:
               k+=1
               continue
            else:
                arr[left][right+1]="0"
        elif move[i]=='U':
            left-=1
            arr[left][right]="1"
            if left<0:
                k+=1
                continue
            else:
                arr[left+1][right]="0"
        elif move[i]=='D':
            left+=1
            arr[left][right]="1"
            if left>n:
                k+=1
                continue
            else:
                arr[left-1][right]="0"
        k-=1
for i in range(0,n):
    for j in range(0,n):
        if arr[i][j]=="1":
            print("%d %d" %(i+1,j+1))
    
