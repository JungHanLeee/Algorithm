#나의 풀이
def solution(answers):
    answers=list(answers)
    cnt=len(answers)
    i=1
    arr1=[]
    arr2=[]
    arr3=[]
    while(cnt>0):
        if i>5:
            i=1
        arr1.append(i)
        i+=1
        cnt-=1
    cnt=len(answers)
    i=1
    j=0
    for i in range(cnt):
        if i%2==0:
            arr2.append(2)
        elif i<=3:
            arr2.append(i)
            j=i+1
        else:
            if j==2:
                j=3
            arr2.append(j)
            j+=1
            if j>5:
                j=1
    cnt=len(answers)
    i=1
    j=1
    z=2
    for i in range(0,cnt):
        if i==0 or i%5==0:
            arr3.append(3)
            if len(arr3)==cnt:
                break
            else:
                arr3.append(3)
        else:
            if i==1 or i==j:
                arr3.append(1)
                if len(arr3)==cnt:
                    break
                else:
                    arr3.append(1)
                j=i+5
            elif i==2 or i==k:
                arr3.append(2)
                if len(arr3)==cnt:
                    break
                else:
                    arr3.append(2)
                k=i+5
            elif i==3 or i==z:
                arr3.append(4)
                if len(arr3)==cnt:
                    break
                else:
                    arr3.append(4)
                z=i+5
            elif i==4 or i==x:
                arr3.append(5)
                if len(arr3)==cnt:
                    break
                else:
                    arr3.append(5)
                x=i+5
        if len(arr3)==cnt:
            break
    a=0
    b=0
    c=0
    for i in range(len(answers)):
        if arr1[i]==int(answers[i]):
            a+=1
        if arr2[i]==int(answers[i]):
            b+=1
        if arr3[i]==int(answers[i]):
            c+=1
    result=[a,b,c]
    final=[]
    for i,score in enumerate(result):
        if score==max(result):
            final.append((i+1))
    print(arr1)
    print(arr2)
    print(arr3)
    return final
# 다른사람 풀이
#내 풀이에 비해 가독성도 좋고 짧게 코딩한게 너무 멋있다
#좀 더 고민해보고 문제를 푸는 방식으로 해봐야겠다
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result