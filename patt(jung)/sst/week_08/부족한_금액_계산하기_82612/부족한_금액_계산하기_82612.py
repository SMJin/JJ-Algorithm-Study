
def solution(price, money, count):
    answer = -1

    for i in range(1, count + 1):
        money -= price * i

    return abs(min(money, 0))


if __name__ == '__main__':
    print(solution(
        3, 20, 4
    ))
