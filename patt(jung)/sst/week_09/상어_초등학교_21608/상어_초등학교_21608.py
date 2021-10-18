import sys
from pprint import pprint

ways = [
    [-1, 0],
    [ 0, 1],
    [ 1, 0],
    [ 0, -1],
]


def find_sit_position(sit, student, likes):
    counts = []
    for i in range(len(sit)):
        for j in range(len(sit)):
            if sit[i][j] != -1: continue
            like_hit_cnt = 0
            empty_cnt = 0
            for i1, j1 in ways:
                if 0 <= i + i1 < len(sit) and 0 <= j + j1 < len(sit):
                    if sit[i + i1][j + j1] in likes:
                        like_hit_cnt += 1
                    elif sit[i + i1][j + j1] == -1:
                        empty_cnt += 1
            counts.append([like_hit_cnt, empty_cnt, i, j])
    sorted_counts = sorted(counts, key=lambda x: (-x[0], -x[1], x[2], x[3]))
    return sorted_counts[0][2], sorted_counts[0][3]


def get_score(sit, like_arr):
    total = 0
    for i in range(len(sit)):
        for j in range(len(sit)):
            hit_cnt = 0
            for i1, j1 in ways:
                y, x = i + i1, j + j1
                if 0 <= y < len(sit) and 0 <= x < len(sit):
                    if sit[y][x] in like_arr[sit[i][j]]:
                        hit_cnt += 1
            if hit_cnt == 1:
                total += 1
            elif hit_cnt == 2:
                total += 10
            elif hit_cnt == 3:
                total += 100
            elif hit_cnt == 4:
                total += 1000
    return total


def main():
    input1 = sys.stdin.readline
    n = int(input1())
    like_arr = [[] for _ in range(n**2 + 1)]
    sit = [[-1] * n for _ in range(n)]
    for _ in range(n**2):
        idx, *likes = map(lambda x: int(x) - 1, input().split())
        like_arr[idx] = likes
        y, x = find_sit_position(sit, idx, set(likes))
        sit[y][x] = idx

    print(get_score(sit, like_arr))


if __name__ == "__main__":
    main()
