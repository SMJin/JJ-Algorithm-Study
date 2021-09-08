import sys
from pprint import pprint


def get_default_visit_arr(n):
    return [False for _ in range(n*2)]


input1 = sys.stdin.readline
answer = [0, 0]
n = int(input1())
a = [list(map(int, input1().split())) for _ in range(n)]
left_visit, right_visit = get_default_visit_arr(n), get_default_visit_arr(n)


def find(x, y, k, color):
    answer[color] = max(answer[color], k)
    if y >= n:
        if y % 2 == 0:
            y = 1
        else:
            y = 0
        x += 1
    if x >= n:
        return
    if a[x][y] and not left_visit[x+y] and not right_visit[x-y+n-1]:
        left_visit[x + y] = right_visit[x - y + n - 1] = True
        find(x, y+2, k+1, color)
        left_visit[x + y] = right_visit[x - y + n - 1] = False
    find(x, y+2, k, color)


def main():
    find(0, 0, 0, 0)
    find(0, 1, 0, 1)
    print(sum(answer))


if __name__ == "__main__":
    main()
