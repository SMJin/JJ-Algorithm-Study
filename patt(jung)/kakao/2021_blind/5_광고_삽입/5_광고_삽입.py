

def time2seconds(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def seconds2time(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    seconds %= 60
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(seconds).zfill(2)}"


def convert_logs(logs):
    st, ed = [], []
    for log in logs:
        a, b = log.split("-")
        st.append(time2seconds(a))
        ed.append(time2seconds(b))
    return st, ed


def solution(play_time, adv_time, logs):
    play_time = time2seconds(play_time)
    adv_time = time2seconds(adv_time)
    logs_start, logs_end = convert_logs(logs)

    total_time = [0 for _ in range(100*60*60)]

    for i in range(len(logs)):
        total_time[logs_start[i]] += 1
        total_time[logs_end[i]] -= 1

    for _ in range(2):
        for i in range(1, play_time):
            total_time[i] += total_time[i-1]

    max_time = total_time[adv_time]
    answer = 0
    for i in range(adv_time, play_time):
        if max_time < total_time[i] - total_time[i - adv_time]:
            max_time = total_time[i] - total_time[i - adv_time]
            answer = i - adv_time + 1

    return seconds2time(answer)


if __name__ == "__main__":
    print(solution(
        "02:03:55",
        "00:14:15",
        [
            "01:20:15-01:45:14",
            "00:40:31-01:00:00",
            "00:25:50-00:48:29",
            "01:30:59-01:53:29",
            "01:37:44-02:02:30"
        ],
    )) # "01:30:59"

    # solution(
    #     "99:59:59",
    #     "25:00:00",
    #     [
    #         "69:59:59-89:59:59",
    #         "01:00:00-21:00:00",
    #         "79:59:59-99:59:59",
    #         "11:00:00-31:00:00"
    #     ],
    # ) # "01:00:00"
