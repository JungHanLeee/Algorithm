#새로운 배열을 만드는데 그 배열의 값은 100에서 처음 배열갑을 뺀 값을 넣는다
def solution(progresses, speeds):
    cnt=1
    answer = []
    for i in range(len(progresses)):
        if ((100-progresses[i])/speeds[i]).is_integer():
            progresses[i]=int((100-progresses[i])/speeds[i])
        else:
            progresses[i]=(100-progresses[i])//speeds[i]+1
    #위처럼 복잡하지않게 가능
    '''
    daysLeft=list(map(lambda x:(ceil((100-progresses[x]/speeds[x]))
    '''
    for i in range(len(progresses)):
        try:
            #뒷 숫자보다 작다면 바로 삽입, 카운트 초기화
            if progresses[i]<progresses[i+1]:
                answer.append(cnt)
                cnt=1
            else:
                #5 10 1 1 20 1
            #0  #0  1 1 1 20 1
            #1  #0  1 1         cnt2
            #2  #0  1 1 1       cnt3
            #3  #0  0 0 0 20    cnt1
            #4  #0  0 0 0  1 1  cnt2
            #5  #0  0 0 0  e    
                #뒷 숫자보다 크다면 어짜피 뒷 숫자와 같게 만들고 카운트+1
                progresses[i+1]=progresses[i]
                cnt+=1
        #배열의 끝에선 앞 숫자와 같으므로 바로 삽입
        except IndexError:
            answer.append(cnt)
    return answer