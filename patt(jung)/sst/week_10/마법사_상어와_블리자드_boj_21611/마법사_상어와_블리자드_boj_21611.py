import sys

DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)


def get_serialized(a):
    t = int((len(a) + 1) / 2 - 1)
    x, y = t, t
    d = 0
    v = [[False] * len(a) for _ in range(len(a))]
    v[x][y] = True
    ret = [a[x][y], ]
    while True:
        nx, ny = x + DELTA[(d + 1) % 4][0], y + DELTA[(d + 1) % 4][1]
        if not v[nx][ny]:
            d += 1
            x, y = nx, ny
        else:
            x, y = x + DELTA[d % 4][0], y + DELTA[d % 4][1]
        v[x][y] = True
        ret.append(a[x][y])
        if x == y == 0:
            break
    return ret


def get_step1(a, d, s):
    if d == 1:
        x = 7
    elif d == 2:
        x = 3
    elif d == 3:
        x = 1
    else:
        x = 5
    removes = [x]
    for i in range(1, s):
        removes.append(removes[-1] + x + 8 * i)

    remove_idx = 0
    ret = []
    for i in range(len(a)):
        if remove_idx < len(removes) and i == removes[remove_idx]:
            remove_idx += 1
            continue
        ret.append(a[i])

    return ret


def get_step2(a):
    flag = True
    while flag:
        flag = False
        t = 0
        temp, cache = [0], []
        for i in range(1, len(a)):
            if a[i] == 0: break
            if t == a[i]:
                cache.append(t)
            else:
                if len(cache) < 4:
                    temp += cache
                else:
                    blow_counts[t - 1] += len(cache)
                    flag = True
                t, count = a[i], 1
                cache = [t]
        if cache:
            if len(cache) < 4:
                temp += cache
            else:
                blow_counts[t - 1] += len(cache)
        a = temp
    return a


def get_step3(a, full):
    if len(a) == 1:
        return a
    t, count = a[1], 1
    ret = [0]
    for i in range(2, len(a)):
        if t == a[i]:
            count += 1
        else:
            ret += [count, t]
            t, count = a[i], 1
        if len(ret) == full:
            break
    if count and len(ret) < full:
        ret += [count, t]
    return ret


def get_final(a):
    ret = 0
    for i in range(len(a)):
        ret += a[i] * (i + 1)
    return ret


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    magic = [list(map(int, input().split())) for _ in range(m)]

    a = get_serialized(mat)
    for i in range(len(magic)):
        a = get_step1(a, magic[i][0], magic[i][1])
        a = get_step2(a)
        a = get_step3(a, n * n)
    print(get_final(blow_counts))


if __name__ == "__main__":
    blow_counts = [0, 0, 0]
    main()
