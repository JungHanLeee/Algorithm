from typing import List
from self import self

class Solutions:
    def arrayPairSum(self,nums:List[int])->int:
        sum=0
        pair=[]
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair)==2:
                sum+=min(pair)
                print(pair)
                pair=[]
        return sum
numbers=[1,4,3,2]
print(Solutions.arrayPairSum(self,numbers))