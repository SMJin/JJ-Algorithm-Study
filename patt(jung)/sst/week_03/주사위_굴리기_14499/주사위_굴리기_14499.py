import sys
from typing import List

# →, ←, ↑, ↓
directions = (
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0),
)


class Dice:
    def __init__(self, arr: List[List[int]], N, M, x, y):
        self.arr = arr
        self.N = N
        self.M = M
        self.x = x
        self.y = y
        self.top = 0
        self.bottom = 0
        self.front = 0
        self.back = 0
        self.right = 0
        self.left = 0

    def execute(self, command: int):
        x1, y1 = directions[command - 1]
        if 0 <= self.x + x1 < self.N and 0 <= self.y + y1 < self.M:
            self.x, self.y = self.x + x1, self.y + y1
            if command == 1:
                self._east()
            elif command == 2:
                self._west()
            elif command == 3:
                self._north()
            else:
                self._south()

            if self.arr[self.x][self.y] > 0:
                self.bottom = self.arr[self.x][self.y]
                self.arr[self.x][self.y] = 0
            else:
                self.arr[self.x][self.y] = self.bottom

            print(self.top)

    def _east(self):
        self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom

    def _west(self):
        self.top, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.top

    def _north(self):
        self.top, self.front, self.bottom, self.back = self.back, self.top, self.front, self.bottom

    def _south(self):
        self.top, self.front, self.bottom, self.back = self.front, self.bottom, self.back, self.top


def main():

    N, M, x, y, _ = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    commands = list(map(int, sys.stdin.readline().split()))
    dice = Dice(arr, N, M, x, y)

    for command in commands:
        dice.execute(command)


if __name__ == "__main__":
    main()
