import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().strip())) for _ in range(n)]

# print(matrix)
right_arr = []
check = min(n,m)
len_quad = [1,]
for i in range(n):
    for j in range(m):
        for k in range(check):
            if (i+k)<n and (j+k)<m and matrix[i][j] == matrix[i][j+k] == matrix[i+k][j] ==  matrix[i+k][j+k]:                            
                len_quad.append((k+1)**2)
        # continue
print(max(len_quad))