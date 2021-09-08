import sys


def main():
    input1 = sys.stdin.readline

    n, s = map(int, input1().split())
    a = list(map(int, input1().split()))

    cur1, cur2 = 0, 0
    shortest = n
    part_sum = a[0]

    while cur1 < n and cur2 < n:
        if part_sum >= s:
            if shortest > cur2 - cur1:
                shortest = cur2 - cur1
            part_sum -= a[cur1]
            cur1 += 1
        else:
            cur2 += 1
            if cur2 == n:
                break
            part_sum += a[cur2]
    print(shortest + 1 if shortest != n else 0)


if __name__ == "__main__":
    main()
