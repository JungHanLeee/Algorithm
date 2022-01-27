# 동명이인이 여러명 있을 수 있음
# participant와 completion을 정렬한 후 같은 인덱스에 해당하는 값이 다르다면
# 그 인원은 통과하지 못한 것 이기에 return 해준다
# IndexError가 생긴다면 participant의 마지막 인원이 통과하지 못한 것것participant =["mislav", "stanko", "mislav", "ana"]
def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(participant)):
        try:
            if participant[i] != completion[i]:
                answer = participant[i]
                break
        except IndexError:
            answer = participant[i]
    return answer

# 다른사람 풀이 Counter이용
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# Hash이용
def solution(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer