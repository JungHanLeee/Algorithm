#n/2의 개수를 선택하는데 최대한 많은 종류의 포켓몬을 골라야 함
#골라야하는 수가 종류보다 작다면      #골라야하는 수가 종류보다 크다면
#종류-(종류-골라야하는 개수)         # 골라야하는 개수-(골라야하느 개수-종류)
def solution(nums):
    get=int(len(nums)/2)
    nums=sorted(nums)
    cnt=[]
#1
    for i in range(len(nums)):
        if nums[i] in cnt:
            continue
        else:
            cnt.append(nums[i])
#2
    if get<len(cnt):
        print(len(cnt)-(len(cnt)-get))
    elif get>len(cnt):
        print(get-(get-len(cnt)))
    else:
        print(len(cnt))
#오답노트
#1 set함수를 이용해서 중복을 없앨 수 있다
#cnt=list(set(nums))

#2 min함수를 이용한 한줄코딩
# return min(len(nums)/2,len(set(nums))

#2 내가 한 방법보다 조금더 간결한 버전
# if len(nums)/2>len(cnt):
#    answer=len(cnt)
# else:
#    answer=len(nums)/2
