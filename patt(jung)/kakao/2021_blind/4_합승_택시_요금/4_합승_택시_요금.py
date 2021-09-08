from pprint import pprint


def solution(n, s, a, b, fares):
    tree = [[10000001] * (n + 1) for _ in range(n + 1)]
    for i in range(len(fares)):
        x, y, c = fares[i]
        tree[x][y] = tree[y][x] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    tree[i][j] = 0
                    continue
                if tree[i][j] > tree[i][k] + tree[k][j]:
                    tree[i][j] = tree[i][k] + tree[k][j]

    answer = tree[s][a] + tree[s][b]
    for i in range(1, n + 1):
        if answer > tree[s][i] + tree[i][a] + tree[i][b]:
            answer = tree[s][i] + tree[i][a] + tree[i][b]
    return answer


if __name__ == "__main__":
    print(solution(
        6, 4, 6, 2,
        [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    ))  # 82

    print(solution(
        7, 3, 4, 1,
        [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    ))  # 14

    print(solution(
        6, 4, 5, 6,
        [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
    ))  # 18
