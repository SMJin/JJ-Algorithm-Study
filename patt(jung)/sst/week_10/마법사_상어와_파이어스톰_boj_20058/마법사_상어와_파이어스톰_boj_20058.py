import sys
from collections import deque

DELTA = (-1, 0), (0, 1), (1, 0), (0, -1)


def range_check(a, b):
    for i in range(len(a)):
        if not 0 <= a[i] < b:
            return False
    return True


def rotate(a, na, x, y, length):
    for i in range(x, x + length):
        for j in range(y, y + length):
            na[j - y + x][(y + length - 1) - (i - x)] = a[i][j]


def melt(a):
    changed = []
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 0:
                continue
            positive_cnt = 0
            for dx, dy in DELTA:
                nx, ny = i + dx, j + dy
                if not range_check((nx, ny), len(a)):
                    continue
                if a[nx][ny] > 0:
                    positive_cnt += 1
            if positive_cnt < 3:
                changed.append((i, j))
    for i, j in changed:
        a[i][j] -= 1


def bfs(a, v, i, j):
    ret1, ret2 = a[i][j], 1
    q = deque([[(i, j)]])
    while q:
        popped = q.popleft()
        for x, y in popped:
            nxt = []
            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if not range_check((nx, ny), len(a)) or v[nx][ny]:
                    continue
                v[nx][ny] = True
                if a[nx][ny] <= 0:
                    continue
                nxt.append((nx, ny))
                ret1 += a[nx][ny]
                ret2 += 1
            q.append(nxt)
    return ret1, ret2


def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(2 ** n)]
    ls = list(map(int, input().split()))
    total_length = 2 ** n

    for l in ls:
        if l:
            block_num = 2 ** (n - l)
            block_len = 2 ** l
            na = [a_line.copy() for a_line in a]
            for i in range(block_num):
                for j in range(block_num):
                    rotate(a, na, i * block_len, j * block_len, block_len)
            a = na
        melt(a)

    v = [[False] * total_length for _ in range(total_length)]
    result, maximum = 0, 0
    for i in range(total_length):
        for j in range(total_length):
            if not v[i][j] and a[i][j] > 0:
                v[i][j] = True
                sumi, count = bfs(a, v, i, j)
                maximum = max(count, maximum)
                result += sumi
    print(f"{result}\n{maximum}")


if __name__ == "__main__":
    main()
