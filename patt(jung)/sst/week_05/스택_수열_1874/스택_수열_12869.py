from collections import deque


def main():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    idx = 0
    stack = deque([])
    cmd = []
    for i in range(1, N+1):
        stack.append(i)
        cmd.append('+')

        while stack and stack[-1] == arr[idx]:
            stack.pop()
            cmd.append('-')
            idx += 1

    if len(cmd) == 2 * N:
        print('\n'.join(cmd))
    else:
        print("NO")


if __name__ == "__main__":
    main()
