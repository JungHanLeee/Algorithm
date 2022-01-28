from typing import List

def trap(self, height:List[int])->int:
    stack=[]
    volume=0

    for i in range(len(height)):
        #변곡점을 만나는 경우
        while stack and height[i]>height[stack[-1]]:
            #스택에서 꺼낸다
            top=stack.pop()
            if not len(stack):
                break
            #이전과의 차이만큼 물 높이 처리
            distanse=i-stack[-1]-1
            water=min(height[i],height[stack[-1]])-height[top]

            volume+=distanse*water
        stack.append(i)
    return volume