from itertools import combinations
from collections import defaultdict as dd


def solution(orders, course):
    answer = []

    arr = [dd(int) for _ in range(course[-1] + 1)]
    for i in range(len(orders)):
        order = orders[i]
        for j in course:
            for p in list(combinations(list(order), j)):
                arr[j][''.join(sorted(p))] += 1
    for i in course:
        arr[i] = sorted(arr[i].items(), key=lambda x: x[1], reverse=True)
        value = None
        for k, v in arr[i]:
            if v < 2:
                continue
            if value is None:
                value = v
            if v == value:
                answer.append(k)
            else:
                break
    answer = sorted(answer)

    return answer


if __name__ == "__main__":
    print(solution(
        ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
        [2,3,4]
    ))  # ["AC", "ACDE", "BCFG", "CDE"]

    print(solution(
        ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
        [2,3,5]
    ))  # ["ACD", "AD", "ADE", "CD", "XYZ"]

    print(solution(
        ["XYZ", "XWY", "WXA"],
        [2,3,4]
    ))  # ["ACD", "AD", "ADE", "CD", "XYZ"]
