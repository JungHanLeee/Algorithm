location=input()
l=list(location)
cnt=0
x=(ord(l[0])-96) # 열의 값
y=int(l[1])      # 행의 값


for a in range(0,1):
    if (x-2)>0 and (y-1)>0:
        cnt+=1
    for b in range(0,1):
        if (x-2)>0 and (y+1)<9:
            cnt+=1
        for a in range(0,1):
            if (x-1)>0 and (y+2)<9:
                cnt+=1
            for b in range(0,1):
                if (x-1)>0 and (y-2)>0:
                    cnt+=1
                for a in range(0,1):
                    if (x+1)<9 and (y-2)>0:
                        cnt+=1
                    for b in range(0,1):
                        if (x+1)<9 and (y+2)<9:
                            cnt+=1
                        for a in range(0,1):
                            if (x+2)<9 and (y+1)<9:
                                cnt+=1
                            for b in range(0,1):
                                if (x+2)<9 and (y-1)>0:
                                    cnt+=1
                                    
print(cnt)

#풀이
location=input()
row=int(location[1])
column=(ord(locationl[0])-96)

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0;
for strp in steps:
    next_row=row+step[0]
    next_column=column+step[1]
    if next_row>=1 next_row <9 and next_column>=1 and next_column<=8:
        result+=1
print(result)
