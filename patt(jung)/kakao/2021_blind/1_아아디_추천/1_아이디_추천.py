
def is_valid(c: str):
    ch = ord(c)
    if 97 <= ch <= 122 or c in ('-', '_', '.') or c.isdigit():
        return True
    else:
        return False


def solution(new_id):
    answer = ''

    # 1
    new_id = new_id.lower()

    # 2
    tmp = ''
    for c in new_id:
        if is_valid(c):
            tmp += c
    new_id = tmp

    # 3
    tmp = new_id[0]
    for i in range(1, len(new_id)):
        if '.' == tmp[-1] == new_id[i]:
            pass
        else:
            tmp += new_id[i]
    new_id = tmp

    # 4
    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5
    if len(new_id) == 0:
        new_id = 'a'

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


if __name__ == "__main__":
    print(solution(
        "...!@BaT#*..y.abcdefghijklm"
    )) # "bat.y.abcdefghi"

    print(solution(
        "z-+.^."))
    print(solution(
        "=.="))
    print(solution(
        "123_.def"))
    print(solution(
        "abcdefghijklmn.p"))
