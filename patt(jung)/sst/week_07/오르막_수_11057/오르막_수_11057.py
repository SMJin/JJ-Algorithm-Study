
def main():
    n = int(input())

    d = [[0] * 10 for _ in range(n + 1)]

    for i in range(10):
        d[0][i] = 1
    for i in range(1, n + 1):
        tmp = 0
        for j in range(10):
            tmp += d[i - 1][j]
            d[i][j] = tmp % 10007

    print(d[n][9])


if __name__ == "__main__":
    main()
