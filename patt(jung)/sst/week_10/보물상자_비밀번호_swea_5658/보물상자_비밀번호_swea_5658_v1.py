from typing import *


def get_split(numbers, bound) -> List[str]:
    cache = ''
    ret = []
    for i in range(len(numbers)):
        cache += numbers[i]
        if len(cache) == bound:
            ret.append(cache)
            cache = ''
    return ret


def main():
    for T in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        numbers = input()
        bound = len(numbers) // 4
        s = set()
        for i in range(bound):
            split = get_split(numbers, bound)
            for y in list(map(lambda x: int(x, 16), split)):
                if y not in s:
                    s.add(y)
            numbers = numbers[-1] + numbers[:-1]
        a = sorted(list(s), reverse=True)
        print(f"#{T} {a[k - 1]}")


if __name__ == "__main__":
    main()
