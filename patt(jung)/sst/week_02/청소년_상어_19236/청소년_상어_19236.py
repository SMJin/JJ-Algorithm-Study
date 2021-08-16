import sys
from pprint import pprint
from typing import List
import copy

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
directions = (
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
)


class Fish:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.number = 0
        self.direction = 0
        self.is_alive = True
        self.is_shark = False

    def __repr__(self):
        return str(self.number)

    def change_pos(self, arr, other):
        arr[self.x][self.y], arr[other.x][other.y] = arr[other.x][other.y], arr[self.x][self.y]
        self.x, other.x = other.x, self.x
        self.y, other.y = other.y, self.y

    def set(self, x, y, number, direction):
        self.x = x
        self.y = y
        self.number = number
        self.direction = direction


def fish_move(arr: List[List[Fish]], fish: Fish):
    for j in range(8):
        a, b = directions[(fish.direction+j) % 8]
        r, c = fish.x + a, fish.y + b
        if 0 <= r < 4 and 0 <= c < 4 and not arr[r][c].is_shark:
            fish.direction = (fish.direction+j) % 8
            fish.change_pos(arr, arr[r][c])
            break


def is_possible_shark_move(arr: List[List[Fish]], shark: Fish, d):
    a, b = directions[shark.direction]
    r, c = shark.x + (a * d), shark.y + (b * d)
    return (0 <= r < 4 and 0 <= c < 4 and arr[r][c].is_alive), r, c


def shark_move(arr: List[List[Fish]], shark: Fish, r, c):
    target = arr[r][c]
    target.is_alive, target.is_shark = False, True
    shark.is_shark = False
    return target


def shark_back(target: Fish, shark: Fish):
    target.is_alive, target.is_shark = True, False
    shark.is_shark = True


def serialize_2d(arr) -> List[Fish]:
    ret = [0 for _ in range(16)]
    for x in arr:
        for y in x:
            ret[y.number] = y
    return ret


def loop(real_fish_2d, shark_r, shark_c, fish_sum):
    fish_2d = copy.deepcopy(real_fish_2d)  # 물고기들 각 좌표에 맞게 들어 있는 2차 리스트
    fish_1d = serialize_2d(fish_2d)  # 물고기들 번호 순으로 들어 있는 1차 리스트
    shark = fish_2d[shark_r][shark_c]
    for i in range(16):
        if fish_1d[i].is_alive:
            fish_move(fish_2d, fish_1d[i])
    results = [fish_sum]
    for i in range(1, 4):
        is_possible, r, c = is_possible_shark_move(fish_2d, shark, i)
        if is_possible:
            target = shark_move(fish_2d, shark, r, c)
            results.append(loop(fish_2d, target.x, target.y, fish_sum + target.number + 1))
            shark_back(target, shark)
    return max(results)


def main():

    arr = []
    for _ in range(4):
        tmp = list(map(int, sys.stdin.readline().split()))
        arr.append([[i-1, j-1] for i, j in zip(tmp[0::2], tmp[1::2])])

    fish_2d = [[Fish() for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            n, d = arr[i][j]
            fish_2d[i][j].set(i, j, n, d)

    fish_2d[0][0].is_alive, fish_2d[0][0].is_shark = False, True
    return loop(fish_2d, 0, 0, fish_2d[0][0].number + 1)


if __name__ == "__main__":
    print(main())
