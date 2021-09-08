import bisect


class Trie:
    def __init__(self, curr=''):
        self.next = dict()
        self.curr = curr
        self.scores = []


def dfs(t, q, idx):
    res = 0
    if len(q)-1 == idx:
        return len(t.scores) - bisect.bisect_left(t.scores, int(q[-1]))
    if q[idx] == '-':
        for k, v in t.next.items():
            res += dfs(v, q, idx + 1)
    else:
        if q[idx] in t.next:
            nxt = t.next[q[idx]]
            res = dfs(nxt, q, idx + 1)
    return res


def solution(info, query):
    answer = []

    trie = Trie()
    for i in range(len(info)):
        detail = info[i].split()
        tmp_t = trie
        for j in range(len(detail)):
            if j == len(detail) - 1:
                bisect.insort(tmp_t.scores, int(detail[j]))
                continue
            if detail[j] in tmp_t.next:
                t = tmp_t.next[detail[j]]
            else:
                t = Trie(detail[j])
                tmp_t.next[detail[j]] = t
            tmp_t = t

    for i in range(len(query)):
        *q, last = query[i].split(' and ')
        q += last.split()

        answer.append(dfs(trie, q, 0))

    return answer


if __name__ == "__main__":
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
    ))  # [1,1,1,1,2,4]
