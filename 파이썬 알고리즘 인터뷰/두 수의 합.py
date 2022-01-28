from typing import List

#브루트포스 방식 (단점 시간복잡도)
def twoSum(self, nums:List[int],target:int)->List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if((nums[i]+nums[j])==target):
                return [i,j]

#in을 이용한 탐색
def twoSum(self, nums:List[int],target:int)->List[int]:
    for i,n in enumerate(nums):
        complement=target-n
        if complement in nums[i+1:]:
            return [nums.index(n),nums[i+1:].index(complement)+(i+1)]

#첫 번쨰 수를 뺀 결과 키 조회
def twoSum(self, nums:List[int],target:int)->List[int]:
    nums_map={}
    #키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num]=i
    for i,num in enumerate(nums):
        if target-num in nums_map and i != nums_map[target-num]:
            return[i,nums_map[target-num]]

#조회구조 개선
def twoSum(self, nums:List[int],target:int)->List[int]:
    nums_map={}
    #하나의 for문으로 통합
    for i,num in enumerate(nums):
        #딕셔너리는 키값을 기준으로 찾음!!
        if target-num in nums_map:
            return [nums_map[target-num],i]
        nums_map[num]=i

