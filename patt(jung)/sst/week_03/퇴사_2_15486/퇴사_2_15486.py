import sys
from collections import deque


def main():

    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    cache = deque([0] * 52)
    cache[arr[0][0]] = arr[0][1]
    for i in range(1, N):
        t, p = arr[i]
        cache[t + 1] = max(cache[0] + p, cache[1] + p, cache[t + 1])
        cache[1] = max(cache[0], cache[1])
        cache.popleft()
        cache.append(0)
    print(max(cache[0], cache[1]))


if __name__ == "__main__":
    main()


# 참고 코드
# r = range
# d = [0]
# n, *l = map(int, open(0).read().split())
# for i, j in zip(l[-2::-2], l[-1::-2]):
#     d += [max(d[-1], d[-1] if i > len(d) else d[-i] + j)]
# print(d[-1])
