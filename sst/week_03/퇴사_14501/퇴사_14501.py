import sys


def main():

    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    cache = [0, 0, 0, 0, 0, 0, 0]
    cache[arr[0][0]] = arr[0][1]
    for i in range(1, N):
        t, p = arr[i]
        cache[t + 1] = max(cache[0] + p, cache[1] + p, cache[t + 1])
        cache[0] = max(cache[0], cache[1])
        for k in range(2, 7):
            cache[k-1] = cache[k]
        cache[6] = 0
    print(max(cache[0], cache[1]))


if __name__ == "__main__":
    main()
