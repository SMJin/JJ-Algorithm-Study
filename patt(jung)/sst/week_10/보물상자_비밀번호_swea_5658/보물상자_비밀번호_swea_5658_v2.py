
def main():
    for T in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        numbers = input()
        bound = len(numbers) // 4

        cache = numbers[:bound]
        s = {int(cache, 16)}
        for i in range(bound, len(numbers) + bound):
            cache = cache[1:] + numbers[i % len(numbers)]
            s.add(int(cache, 16))
        a = sorted(list(s), reverse=True)
        print(f"#{T} {a[k - 1]}")


if __name__ == "__main__":
    main()
