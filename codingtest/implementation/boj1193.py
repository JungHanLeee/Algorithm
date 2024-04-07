import sys
input = sys.stdin.readline


x = int(input())
line = 1

while x>line:
    x-=line
    line+=1
if line % 2 != 0:
    i = line-x+1
    j = x
else:
    i = x
    j = line-x+1

print(str(i) + '/' + str(j))

# 전체 구현 (시간초과)
# x =  int(input())
# arr = []
# i = 1
# j = 1
# temp=0
# result = ''
# while len(arr) <= x:
#     if i == 1 and j == 1:
#         arr.append([i,j])
#         j+=1
#         continue
#     if i == 1:
        
#         arr.append([i,j])
#         while j>1:
#             j-=1
#             i+=1
#             arr.append([i,j])
#         continue
#     if j == 1:
#         i+=1
#         arr.append([i,j])
#         while i>1:
#             i-=1
#             j+=1
#             arr.append([i,j])
#         j+=1
#         continue
# result = str(arr[x-1][0]) +'/' + str(arr[x-1][1])
# print(result)
# print(arr)
# print(arr[x-1])
