false=False
true=True
absolutes=[4,7,12]
signs=[true,false,true]

def solution(absolutes,signs):
    for i in range(len(absolutes)):
        if signs[i]==false:
            absolutes[i]=absolutes[i]*-1
    return print(sum(absolutes))

solution(absolutes,signs)
