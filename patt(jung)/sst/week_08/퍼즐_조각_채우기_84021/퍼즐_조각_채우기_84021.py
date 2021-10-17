from pprint import pprint

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))


def copy_2d(arr):
    return [a.copy() for a in arr]


def array_value_switcher(func):
    def func_wrapper(arr1, x1, y1, arr2, x2, y2, offset):
        arr2[x2][y2] = -1
        result = func(arr1, x1, y1, arr2, x2, y2, offset)
        arr2[x2][y2] = 0
        return result

    return func_wrapper


def find(arr, x, y, t, target):
    arr[x][y] = t
    area_sum = 1
    for d_x, d_y in dirs:
        if not (0 <= x + d_x < len(arr) and 0 <= y + d_y < len(arr)):
            continue
        if arr[x + d_x][y + d_y] == target:
            area_sum += find(arr, x + d_x, y + d_y, t, target)
    return area_sum


def is_in_range(n, args):
    for arg in args:
        if not 0 <= arg < n:
            return False
    return True


def find_check(arr1, x1, y1, arr2, x2, y2, offset, cnt):
    temp = arr2[x2][y2]
    arr2[x2][y2] = -1
    result = cnt
    for i in range(4):
        d_x2, d_y2 = dirs[(i + offset) % len(dirs)]
        d_x1, d_y1 = dirs[i]
        if is_in_range(len(arr1), (x2 + d_x2, y2 + d_y2)):
            if not is_in_range(len(arr1), (x1 + d_x1, y1 + d_y1)):
                continue
        else:
            continue

        if arr2[x2 + d_x2][y2 + d_y2] > 1:
            if arr1[x1 + d_x1][y1 + d_y1] < 0:
                result = find_check(arr1, x1 + d_x1, y1 + d_y1, arr2, x2 + d_x2, y2 + d_y2, offset, result + 1)
            else:
                continue
        else:
            if arr1[x1 + d_x1][y1 + d_y1] < 0:
                continue
    arr2[x2][y2] = temp
    return result


def fit_check(x, y, game_board, table, space, puzzle):
    for i in range(4):
        # if puzzle[0] == 1 and puzzle[1] == 2 and x == 4 and y == 3:
        #     print()
        result = find_check(game_board, x, y, table, puzzle[0], puzzle[1], i, 1)
        if result == puzzle[2] == space[2]:
            # print(x, y, puzzle[0], puzzle[1], result, puzzle[2])
            return True
    return False


def fit_dfs(x, y, game_board, table, space, puzzle):
    if fit_check(x, y, game_board, table, space, puzzle):
        return True
    game_board[x][y] -= 1
    for d_x, d_y in dirs:
        if not is_in_range(len(game_board), (x + d_x, y + d_y)):
            continue
        if game_board[x + d_x][y + d_y] > game_board[x][y] and game_board[x + d_x][y + d_y] != 1:
            if fit_dfs(x + d_x, y + d_y, game_board, table, space, puzzle):
                return True
    return False


def loop(game_board, table, spaces, spaces_idx, puzzles, puzzles_idx):
    if spaces_idx == len(spaces) or puzzles_idx == len(puzzles):
        return 0
    puzzle = puzzles[puzzles_idx]
    results = [0, ]
    for i in range(spaces_idx, len(spaces)):
        space = spaces[i]
        if space[3] and space[2] >= puzzle[2]:
            is_fit = fit_dfs(space[0], space[1], game_board, table, space, puzzle)
            if is_fit:
                space[3] = False
                results.append(loop(game_board, table, spaces, i + 1, puzzles, puzzles_idx + 1) + puzzle[2])
                space[3] = True
            # else:
            #     results.append(loop(game_board, table, spaces, i + 1, puzzles, puzzles_idx))
        elif space[3]:
            results.append(loop(game_board, table, spaces, i, puzzles, puzzles_idx + 1))
        else:
            results.append(loop(game_board, table, spaces, i + 1, puzzles, puzzles_idx + 1))
    return max(results)


def solution(game_board, table):
    answer = -1

    t = 2
    puzzles = []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1:
                area = find(table, i, j, t, 1)
                puzzles.append([i, j, area])
                t += 1
    puzzles = sorted(puzzles, key=lambda x: x[2], reverse=True)

    spaces = []
    for i in range(len(table)):
        for j in range(len(table)):
            if game_board[i][j] == 0:
                area = find(game_board, i, j, -1, 0)
                spaces.append([i, j, area, True])
    spaces = sorted(spaces, key=lambda x: x[2], reverse=True)

    return loop(game_board, table, spaces, 0, puzzles, 0)


if __name__ == '__main__':
    print(solution(
        [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0]],
        [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0, 0]]
    ))  # 14
