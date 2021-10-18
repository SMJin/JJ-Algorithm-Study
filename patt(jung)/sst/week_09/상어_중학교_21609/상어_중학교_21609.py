import sys
from pprint import pprint
from collections import deque

ways = [
    [-1, 0],
    [ 0, 1],
    [ 1, 0],
    [ 0, -1],
]


def find_block_groups_step2(arr, i, j, t, seqs, seq_id):
    q = deque([[[i, j]]])
    t_size, rainbow_size = 1, 0
    arr[i][j][1] = seq_id
    while q:
        popped = q.popleft()
        nxt = []
        for y, x in popped:
            for i1, j1 in ways:
                i2, j2 = y + i1, x + j1
                if not (0 <= i2 < len(arr) and 0 <= j2 < len(arr)):
                    continue
                if arr[i2][j2][0] in (t, 0) and arr[i2][j2][1] not in seqs and arr[i2][j2][1] != seq_id + 1:
                    nxt.append([i2, j2])
                    if arr[i2][j2][0] == t:
                        arr[i2][j2][1] = seq_id
                        t_size += 1
                    else:
                        arr[i2][j2][1] = seq_id + 1
                        rainbow_size += 1
        if nxt:
            q.append(nxt)
    return t_size, rainbow_size


def find_block_groups_step1(arr, seq_id):
    seqs = set()
    blocks = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j][0] > 0 and arr[i][j][1] not in seqs:
                seqs.add(seq_id)
                t_size, rainbow_size = find_block_groups_step2(arr, i, j, arr[i][j][0], seqs, seq_id)
                if t_size + rainbow_size > 1:
                    arr[i][j][1] = seq_id
                    blocks.append([t_size + rainbow_size, rainbow_size, i, j])
                else:
                    seqs.remove(seq_id)
                seq_id += 2
    sorted_blocks = sorted(blocks, key=lambda x: [x[0], x[1], x[2], x[3]], reverse=True)
    return sorted_blocks, seq_id


def scrap_score(arr, i, j, t):
    arr[i][j] = [-100, -100]
    q = deque([[[i, j]]])
    while q:
        popped = q.popleft()
        nxt = []
        for y, x in popped:
            for i1, j1 in ways:
                i2, j2 = y + i1, x + j1
                if not (0 <= i2 < len(arr) and 0 <= j2 < len(arr)):
                    continue
                if arr[i2][j2][0] in (t, 0):
                    nxt.append([i2, j2])
                    arr[i2][j2] = [-100, -100]
        if nxt:
            q.append(nxt)


def activate_gravity_step2(arr, i, j):
    if i < len(arr) - 1 and arr[i + 1][j][0] == -100:
        arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
        activate_gravity_step2(arr, i + 1, j)


def activate_gravity_step1(arr):
    if len(arr) == 1:
        return
    for i in range(len(arr) - 2, -1, -1):
        for j in range(len(arr)):
            if arr[i][j][0] >= 0:
                activate_gravity_step2(arr, i, j)


def spin(arr):
    new_arr = [[0] * len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            new_arr[len(arr) - j - 1][i] = arr[i][j]
    return new_arr


def main():
    input1 = sys.stdin.readline
    n, m = map(int, input1().split())
    arr = [list(map(lambda x1: [int(x1), -1], input1().split())) for _ in range(n)]

    score = 0
    seq_id = 1
    while True:
        blocks, seq_id = find_block_groups_step1(arr, seq_id)
        if blocks:
            y, x = blocks[0][2], blocks[0][3]
            scrap_score(arr, y, x, arr[y][x][0])
            score += blocks[0][0] ** 2

            activate_gravity_step1(arr)
            arr = spin(arr)
            activate_gravity_step1(arr)
        else:
            break
    print(score)


if __name__ == "__main__":
    main()
