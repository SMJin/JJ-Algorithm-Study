import sys
from pprint import pprint


# ←, ↓, →, ↑
directions = (
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
)


rate = (
    (0, 0, 2, 0, 0),
    (0, 10, 7, 1, 0),
    (5, -1, 0, 0, 0),
    (0, 10, 7, 1, 0),
    (0, 0, 2, 0, 0)
)


def get_overed_sand_sum(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i < 2 or len(arr) - 2 <= i or j < 2 or len(arr) - 2 <= j:
                res += arr[i][j]
    return res


def scatter_sand(x, y, range1, range2, arr, alpha_x, alpha_y, rotate=False):
    scatter_sum = 0
    for i1, i2 in zip(range1, range(5)):
        for j1, j2 in zip(range2, range(5)):
            if rate[i2][j2] > 0:
                s = int(arr[x][y] * rate[i2][j2] / 100)
                scatter_sum += s
                if rotate:
                    arr[j1][i1] += s
                else:
                    arr[i1][j1] += s
    arr[alpha_x][alpha_y] += (arr[x][y] - scatter_sum)
    arr[x][y] = 0


def get_rate_range(x, y, d_idx):
    rotate = False
    if d_idx == 0:
        range1, range2 = range(x-2, x+3), range(y-2, y+3)
    elif d_idx == 1:
        range1, range2 = range(y-2, y+3), range(x+2, x-3, -1)
        rotate = True
    elif d_idx == 2:
        range1, range2 = range(x+2, x-3, -1), range(y+2, y-3, -1)
    else:
        range1, range2 = range(y+2, y-3, -1), range(x-2, x+3)
        rotate = True
    return range1, range2, rotate, x + directions[d_idx][0], y + directions[d_idx][1]


def tornado(x, y, arr, direction):
    range1, range2, rotate, alpha_x, alpha_y = get_rate_range(x, y, direction)
    scatter_sand(x, y, range1, range2, arr, alpha_x, alpha_y, rotate)


def get_next_xy_and_direction(check_arr, d_idx, x, y):
    nxt_idx = (d_idx + 1) % 4
    n_x, n_y = x + directions[nxt_idx][0], y + directions[nxt_idx][1]
    if check_arr[n_x][n_y]:
        x, y = x + directions[d_idx][0], y + directions[d_idx][1]
    else:
        x, y = n_x, n_y
        d_idx += 1
    return d_idx, x, y


def main():

    N = int(sys.stdin.readline())
    arr = [list(map(int, f"0 0 {sys.stdin.readline()} 0 0".split())) for _ in range(N)]
    for _ in range(2):
        arr.insert(0, [0] * (N + 4))
        arr.append([0] * (N + 4))
    n = N + 4
    x, y = n // 2, n // 2
    d_idx = 0
    check_arr = [[False] * n for _ in range(n)]
    check_arr[x][y] = True
    x, y = x + directions[d_idx][0], y + directions[d_idx][1]

    while True:
        d_idx %= 4
        tornado(x, y, arr, d_idx)
        check_arr[x][y] = True

        if x == y == 2:
            break

        d_idx, x, y = get_next_xy_and_direction(check_arr, d_idx, x, y)

    return get_overed_sand_sum(arr)


if __name__ == "__main__":
    print(main())
