import sys

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
directions = (
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
)


def get_around_water_count(arr, r, c):
    """
    대각선 주변에 물이 담긴 바구니의 개수를 찾아 반환.
    """
    cnt = 0
    for i in (1, 3, 5, 7):
        x, y = directions[i][0], directions[i][1]
        if 0 <= r + x < len(arr) and 0 <= c + y < len(arr[0]):
            if arr[r+x][c+y] >= 1:
                cnt += 1
    return cnt


def mark_except_position(arr, clouds):
    """
    구름이 있었던 곳은 바로 다음에 또 구름이 생기지 않도록 예외로 뺌
    """
    excepts = []
    for r, c in clouds:
        excepts.append((r, c, arr[r][c]))
        arr[r][c] = 0
    return excepts


def rollback_excepts(arr, excepts):
    """
    구름이 생기지 않도록 예외로 빼놨던 지역을 원복시킴
    """
    for r, c, x in excepts:
        arr[r][c] = x


def make_clouds(arr):
    clouds = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] >= 2:
                arr[i][j] -= 2
                clouds.append([i, j])
    return clouds


def get_water_cnt(arr):
    ret = 0
    for a in arr:
        ret += sum(a)
    return ret


def main():

    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    moves = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

    for move in moves:
        # 1
        x, y = directions[move[0]-1]
        dist = move[1]
        for cloud in clouds:
            cloud[0] = (cloud[0] + x * dist) % N
            cloud[1] = (cloud[1] + y * dist) % N

        # 2
        for cloud in clouds:
            arr[cloud[0]][cloud[1]] += 1

        # 3
        # clouds.clear()

        # 4
        for cloud in clouds:
            arr[cloud[0]][cloud[1]] += get_around_water_count(arr, cloud[0], cloud[1])

        # 5
        excepts = mark_except_position(arr, clouds)
        clouds = make_clouds(arr)
        rollback_excepts(arr, excepts)

    return get_water_cnt(arr)


if __name__ == "__main__":
    print(main())
