import sys
input = sys.stdin.readline
king, rock, n = map(str, input().rstrip().split())
king = list(king)
rock = list(rock)
len_command = int(n)
col = ['A','B','C','D','E','F','G','H']
king_x = ''
king_y = ''
rock_x = ''
rock_y = ''
king_x = int(king[1])-1
king_y = col.index(king[0])
rock_x = int(rock[1])-1
rock_y = col.index(rock[0])
king_locate = (king_x,king_y)
rock_locate = (rock_x,rock_y)

R = (0,1)     #0
L = (0,-1)    #1
B = (-1,0)     #2
T = (1,0)    #3
RT = (1,1)    #03
LT = (1,-1)   #13
RB = (-1,1)   #02
LB = (-1,-1)  #12

directions = {'R':R, 'L':L, 'B':B, 'T':T, 'RT':RT, 'LT': LT, 'RB':RB, 'LB':LB}
command = [list(map(str, input().rstrip().split())) for _ in range(len_command)]
for i in range(len_command):
    # if command[i][0] not in directions:
    #     continue
    move = directions[command[i][0]]
    new_king_y = king_locate[0] + move[0]
    new_king_x = king_locate[1] + move[1]
    if 0 <= new_king_x < 8 and 0 <= new_king_y < 8:
        if (new_king_y, new_king_x) == rock_locate:
            new_rock_y = rock_locate[0] + move[0]
            new_rock_x = rock_locate[1] + move[1]
            if 0 <= new_rock_x < 8 and 0 <= new_rock_y < 8:
                rock_locate = (new_rock_y, new_rock_x)
                king_locate = (new_king_y, new_king_x)
        else:
            king_locate = (new_king_y, new_king_x)

print("".join(str(col[king_locate[1]])+str(king_locate[0]+1)))
print("".join(str(col[rock_locate[1]])+str(rock_locate[0]+1)))

