def solution(board, moves):
    stack = []
    z = 0
    cnt = 0
    for move in moves:
        x = move - 1
        for i in range(len(board)):
            if board[i][x] != 0:
                stack.append(board[i][x])
                board[i][x] = 0
                break
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                cnt += 2

    return cnt
