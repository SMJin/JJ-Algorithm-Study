
def main():
    *n, zero = map(int, open(0).read().split())
    for N in n:
        dp = [[0] * N for _ in range(N)]
        dp[0][0] = 1
        for i in range(1, N):
            dp[i][0] = dp[i - 1][0] + 1
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp[-1][-1])


if __name__ == "__main__":
    main()
