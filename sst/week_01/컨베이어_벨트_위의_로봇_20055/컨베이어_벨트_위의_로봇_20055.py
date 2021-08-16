import sys
from collections import deque


class Belt:

    zero_belt_cnt = 0

    def __init__(self, duration, is_robot_on=False):
        self.duration = duration
        self.is_robot_on = is_robot_on

    def can_take_robot(self):
        return bool(self.duration) and not self.is_robot_on

    def take_on(self):
        self.duration -= 1
        self.is_robot_on = True
        if self.duration <= 0:
            Belt.zero_belt_cnt += 1

    def take_off(self):
        self.is_robot_on = False


def main():

    N, K = map(int, sys.stdin.readline().split())
    belt_list = list(map(int, sys.stdin.readline().split()))
    belts = deque([Belt(duration) for duration in belt_list])

    cnt = 0
    while True:
        cnt += 1

        # 1
        belts.appendleft(belts.pop())

        # 2
        if belts[N - 1].is_robot_on:
            belts[N - 1].take_off()
        if belts[N - 2].is_robot_on and belts[N - 1].can_take_robot():
            belts[N - 2].take_off()
            belts[N - 1].take_on()  # 로봇이 이동하여 벨트 끝에 도달했을때는 로봇이 곧바로 내리므로 take_on과 동시에 take_off를 한다.
            belts[N - 1].take_off()
        for i in range(N-3, -1, -1):
            if belts[i].is_robot_on and belts[i + 1].can_take_robot():
                belts[i + 1].take_on()
                belts[i].take_off()

        # 3
        if belts[0].can_take_robot():
            belts[0].take_on()

        # 4
        if Belt.zero_belt_cnt >= K:
            break

    return cnt


if __name__ == "__main__":
    print(main())
