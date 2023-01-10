def solution(key, lock):
    M, N=len(key), len(lock)
    board=[[0]*(M*2+N) for _ in range(M*2+N)]
    
    for i in range(N):
        for j in range(N):
            board[i+M][j+M]=lock[i][j]
    
    for i in range(4):
        rotated_key=rotation(i, key)
        for r in range(1, N+M):
            for c in range(1, N+M):
                # print("r :",r,"c :",c, "deg :", i)
                attach(r, c, rotated_key, board)
                # for row in board:
                #     print(row)
                if check(key, rotated_key, board):
                    return True
                detach(r, c, rotated_key, board)
                
    return False

def rotation(deg, arr):
    if deg==0:
        return arr
    N=len(arr)
    rotated_key=[[0]*N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            # 90
            if deg==1:
                rotated_key[c][N-1-r]=arr[r][c]
            # 180
            elif deg==2:
                rotated_key[N-1-r][N-1-c]=arr[r][c]
            # 270
            elif deg==3:
                rotated_key[N-1-c][r]=arr[r][c]
    return rotated_key

def attach(x, y, key, board):
    N=len(key)
    for r in range(N):
        for c in range(N):
            board[x+r][y+c]+=key[r][c]

def detach(x, y, key, board):
    N=len(key)
    for r in range(N):
        for c in range(N):
            board[x+r][y+c]-=key[r][c]

def check(key, lock, board):
    M, N=len(key), len(lock)
    for r in range(N):
        for c in range(N):
            if board[M+r][M+c]!=1:
                return False
    return True
            
solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])