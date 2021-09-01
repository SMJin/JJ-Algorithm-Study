import sys


def main():
    input1 = sys.stdin.readline

    n, m = map(int, input1().split())
    a = sorted([int(input1()) for _ in range(n)], reverse=True)

    cur1, cur2 = 0, 0
    minimum = a[0] - a[-1]
    while cur2 < n and cur1 < n:
        diff = a[cur1] - a[cur2]
        if diff >= m:
            if minimum > diff:
                minimum = diff
            cur1 += 1
        else:
            cur2 += 1
    print(minimum)


if __name__ == "__main__":
    main()
