import re
import collections
from datetime import datetime

ts_regex = re.compile(r"\[(\d\d\d\d-\d\d-\d\d \d\d:\d\d)\] (.+)$")
shift_begin_regex = re.compile(r"Guard #(\d+) begins shift")

Timestamp = collections.namedtuple("Timestamp", ["date", "event"])
Shift = collections.namedtuple("Shift", ["guard", "awake_this_minute"])

def load_timestamps():
    timestamps = []
    for l in open("input_sorted.txt"):
        match = ts_regex.match(l)
        date = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
        timestamps.append(Timestamp(date, match.group(2)))
    return timestamps

def build_shifts(timestamps):
    shifts = []
    timestamps.reverse()
    ts = timestamps.pop()
    match = shift_begin_regex.match(ts.event)
    shift = Shift(match.group(1), [True]*60)
    while(len(timestamps) > 0):
        ts = timestamps.pop()
        match = shift_begin_regex.match(ts.event)
        if (match):
            shifts.append(shift)
            shift = Shift(match.group(1), [True]*60)
        else:
            start = ts
            end = timestamps.pop()
            for i in range(start.date.minute, end.date.minute):
                shift.awake_this_minute[i] = False
    shifts.append(shift)
    return shifts

ts = load_timestamps()
shifts = build_shifts(ts)
for s in shifts:
    print(s)


    

