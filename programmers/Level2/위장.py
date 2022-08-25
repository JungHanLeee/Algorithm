https://school.programmers.co.kr/learn/courses/30/lessons/42578
  
# 1 옷 종류 파악
# 옷 종류에 따른 딕셔너리 만들기
def solution(clothes):
    new_list={}
    answer=1
    for i in range(len(clothes)):
        if clothes[i][-1] not in new_list:
            new_list[clothes[i][-1]]=1
        # 이미 들어있는데 다시 조회됐을 때
        else:
            new_list[clothes[i][-1]]+=1
    
    # print(new_list.items())
    # print(len(new_list)) 옷 종류
    # 각 value+1한 값들을 전부 곱한 후 -1 => 정답
    p=list(new_list.values())
    for i in p:
        answer*=1+i
    answer -= 1
    
    return answer
