import math
n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input())

result = math.inf

for i in range(n-7):
    for j in range(m-7):
        start_W = 0
        start_B = 0
        for col in range(i, i+8):
            for row in range(j, j+8):
                #짝수 번째 칸을
                if (col + row) % 2 == 0:
                    #W로 바꾸는 경우
                    if board[col][row] == 'B':
                        start_W += 1
                    #B로 바꾸는 경우
                    if board[col][row] == 'W':
                        start_B += 1
                #홀수 번째 칸을
                else:
                    #B로 바꾸는 경우
                    if board[col][row] == 'W':
                        start_W += 1
                    #W로 바꾸는 경우
                    if board[col][row] == 'B':
                        start_B += 1
                        
        result = min([result, start_B, start_W])
    
print(result)
