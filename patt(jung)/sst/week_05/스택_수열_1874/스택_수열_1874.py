from collections import deque
import sys


r = sys.stdin.readline


def main():
    N = int(r())
    arr = [int(r()) for _ in range(N)]
    idx = 0
    stack = deque([])
    cmd = ''
    for i in range(1, N+1):
        stack.append(i)
        cmd += '+\n'

        while stack and stack[-1] == arr[idx]:
            stack.pop()
            cmd += '-\n'
            idx += 1

    if stack:
        print('NO')
    else:
        print(cmd)


if __name__ == "__main__":
    main()
