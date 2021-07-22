import sys
from collections import deque

directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
walls = set()


def bfs(arr, x, y):
    cnt = 1
    arr[x][y] = -1
    q = deque([[(x, y)]])
    while q:
        popped = q.popleft()
        nxt = []
        for i, j in popped:
            for a, b in directions:
                if 0 <= i+a < len(arr) and 0 <= j+b < len(arr[0]) and arr[i+a][j+b] in (0, 2):
                    nxt.append((i+a, j+b))
                    cnt += 1
                    arr[i+a][j+b] = -1
        if nxt:
            q.append(nxt)
    return cnt


def spread_virus(arr, N, M):
    virus_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virus_cnt += bfs(arr, i, j)
    return virus_cnt


def not_dup(wall0, wall1, wall2):
    wall = "-".join(map(str, sorted([wall0, wall1, wall2])))
    if wall in walls:
        return False
    else:
        walls.add(wall)
        return True


def make_wall(arr, N, M, wall0):
    wall1, wall2 = 0, 0
    min_virus_cnt = 64
    for i1 in range(N):
        for j1 in range(M):
            if arr[i1][j1] == 0:
                arr[i1][j1] = 1
                wall1 = i1 * M + j1
                for i2 in range(N):
                    for j2 in range(M):
                        if arr[i2][j2] == 0:
                            wall2 = i2 * M + j2
                            if not_dup(wall0, wall1, wall2):
                                arr[i2][j2] = 1
                                min_virus_cnt = min(min_virus_cnt, spread_virus(copy_arr(arr), N, M))
                                arr[i2][j2] = 0
                arr[i1][j1] = 0
    return min_virus_cnt


def copy_arr(arr):
    return [a.copy() for a in arr]


def count_target_num(arr, target):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                cnt += 1
    return cnt


def main():

    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    min_virus_cnt = 64
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                min_virus_cnt = min(min_virus_cnt, make_wall(arr, N, M, i*M+j))
                arr[i][j] = 0

    return N*M - count_target_num(arr, 1) - min_virus_cnt - 3


if __name__ == "__main__":
    print(main())
