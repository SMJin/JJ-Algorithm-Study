import sys


def divide(a, b):
    if a < 0:
        return -(-a // b)
    else:
        return a // b


def loop(arr, idx, res, ops, ret):
    if idx == len(arr):
        ret[0] = max(ret[0], res)
        ret[1] = min(ret[1], res)
        return
    for i, op in enumerate(ops):
        if op > 0:
            if i == 0:
                ops[i] -= 1
                loop(arr, idx + 1, res + arr[idx], ops, ret)
                ops[i] += 1
            elif i == 1:
                ops[i] -= 1
                loop(arr, idx + 1, res - arr[idx], ops, ret)
                ops[i] += 1
            elif i == 2:
                ops[i] -= 1
                loop(arr, idx + 1, res * arr[idx], ops, ret)
                ops[i] += 1
            elif i == 3:
                ops[i] -= 1
                loop(arr, idx + 1, divide(res, arr[idx]), ops, ret)
                ops[i] += 1


def main():

    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    ops = list(map(int, sys.stdin.readline().split()))  # 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수

    ret = [-1000000001, 1000000001]
    for i, op in enumerate(ops):
        if op > 0:
            if i == 0:
                ops[i] -= 1
                loop(arr, 2, arr[0] + arr[1], ops, ret)
                ops[i] += 1
            elif i == 1:
                ops[i] -= 1
                loop(arr, 2, arr[0] - arr[1], ops, ret)
                ops[i] += 1
            elif i == 2:
                ops[i] -= 1
                loop(arr, 2, arr[0] * arr[1], ops, ret)
                ops[i] += 1
            elif i == 3:
                ops[i] -= 1
                loop(arr, 2, divide(arr[0], arr[1]), ops, ret)
                ops[i] += 1
    print(ret[0])
    print(ret[1])


if __name__ == "__main__":
    main()
