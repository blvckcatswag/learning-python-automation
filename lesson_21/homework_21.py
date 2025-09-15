from datetime import datetime


def analyze_log(src_path, dst_path):
    key = "Key TSTFEED0300|7E3E|0400"
    filtered = []

    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if key in line:
                filtered.append(line.strip())

    times = []
    for line in filtered:
        pos = line.find("Timestamp ")
        if pos != -1:
            time_str = line[pos + 10:pos + 18]
            times.append(datetime.strptime(time_str, "%H:%M:%S"))

    with open(dst_path, "w", encoding="utf-8") as out:
        for i in range(len(times) - 1):
            cur = times[i]
            nxt = times[i + 1]
            delta = (cur - nxt).total_seconds()
            if delta < 0:
                delta += 24 * 3600

            if 31 < delta < 33:
                out.write(f"WARNING heartbeat {int(delta)}s between {cur:%H:%M:%S} -> {nxt:%H:%M:%S}\n")
            elif delta >= 33:
                out.write(f"ERROR heartbeat {int(delta)}s between {cur:%H:%M:%S} -> {nxt:%H:%M:%S}\n")


if __name__ == "__main__":
    analyze_log(
        r"C:\Users\User.PC-475\PycharmProjects\learning-python-automation\lesson_21\hblog.txt",
        r"C:\Users\User.PC-475\PycharmProjects\learning-python-automation\lesson_21\hb_test.log"
    )
