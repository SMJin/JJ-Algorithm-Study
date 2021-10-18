import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

point = 0


def range_check(x, y):
    return 0 <= x < n and 0 <= y < n


def rotate(a):
    temp = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n - 1 - j][i] = a[i][j]
    return temp


def gravity(a):
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if a[i][j] < 0: continue
            nx = i + 1
            while True:
                if nx == n or a[nx][j] != -2: break
                nx += 1
            nx -= 1
            if i != nx:
                a[nx][j], a[i][j] = a[i][j], -2
    return a


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def search_dfs(x, y, c):
    v[x][y] = True
    ret, new_ret = dict(), dict()
    ret[(x, y)] = 1
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if not range_check(nx, ny): continue
        if board[nx][ny] < 0 or v[nx][ny]: continue
        if v[nx][ny] == False and (board[nx][ny] == 0 or board[nx][ny] == c):
            new_ret = search_dfs(nx, ny, c)
            ret.update(new_ret)
    return ret


def paint_dfs(x, y, c):
    board[x][y] = -2
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if not range_check(nx, ny): continue
        if board[nx][ny] == 0 or board[nx][ny] == c:
            paint_dfs(nx, ny, c)
    return


while True:
    ok = False
    pick = (0, 0, -1, -1)  # size, rainbow, x, y
    v = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] <= 0: continue
            if v[i][j]: continue
            ret = search_dfs(i, j, board[i][j])
            size, rainbow = len(ret), 0
            for key in ret.keys():
                if board[key[0]][key[1]] == 0:
                    v[key[0]][key[1]] = False
                    rainbow += 1
            if size <= 1: continue
            ok = True
            new_pick = (size, rainbow, i, j)
            pick = max(pick, new_pick)
    if not ok: break
    # 포인트 획득
    point += pick[0] ** 2
    # 선택된 애로부터 다시 paint_dfs
    paint_dfs(pick[2], pick[3], board[pick[2]][pick[3]])
    # 중력
    board = gravity(board)
    # rotate
    board = rotate(board)
    # 중력
    board = gravity(board)
print(point)
