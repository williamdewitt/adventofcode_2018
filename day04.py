from datetime import datetime
import operator
import re

# Part 1
d = {}
guards = {}
with open("day04_input.txt", "r") as f:
    for line in f:
        line = line.replace("[", "")
        (key, val) = line.split("]")
        d[key] = val

guard_id = ""
shift_start = ""
falls_asleep = ""
wakes_up = ""

for key in sorted(d.keys()):
    value = d[key]

    if "Guard" in value:
        shift_start = key
        guard_id = re.search("\d+", d[key]).group(0)
        if guard_id not in guards:
            minutes = [0] * 60
            guards[guard_id] = minutes

    elif "falls asleep" in value:
        falls_asleep = key

    elif "wakes up" in value:
        time_wakes_up = datetime.strptime(key, '%Y-%m-%d %H:%M')
        time_falls_asleep = datetime.strptime(falls_asleep, '%Y-%m-%d %H:%M')

        for x in range(time_falls_asleep.minute, time_wakes_up.minute):
            guards[guard_id][x] = guards[guard_id][x] + 1

sleepiest_guard = 0
longest_nap = 0
sleepiest_minute = 0
for guard, minutes in guards.items():
    if sum(minutes) > longest_nap:
        longest_nap = sum(minutes)
        sleepiest_minute = minutes.index(max(minutes))
        sleepiest_guard = guard
    
print("Answer: {}".format(int(sleepiest_guard) * sleepiest_minute))


# Part 2
popular_minute = 0
popular_guard = 0
max_min = 0
for guard, minutes in guards.items():
    if max(minutes) > max_min:
        max_min = max(minutes)
        popular_minute = minutes.index(max(minutes))
        popular_guard = int(guard)

print("Answer: {}".format(int(popular_guard) * popular_minute))
