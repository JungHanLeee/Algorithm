board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
stack=[]
z=0
cnt=0
for move in moves:
    x=move-1
    for i in range(len(board)):
        if board[i][x]>0:
            stack.append(board[i][x])
            board[i][x]=0
            break
    if len(stack)>1:
        if stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
            cnt+=2
print(cnt)
print(stack)
for i in range(len(board)):
    for j in range(len(board)):
        print(board[i][j],end="")
    print("")

