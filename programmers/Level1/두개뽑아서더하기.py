https://school.programmers.co.kr/learn/courses/30/lessons/68644
  
def solution(numbers):
    arr=[]
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] not in arr:
                if numbers[i]+numbers[j]==8:
                    print(numbers[i],numbers[j])
                arr.append(numbers[i]+numbers[j])
    arr=sorted(arr)
    return arr
