from collections import Counter

text_file = open("day02_input.txt", "r")
input = text_file.read().split('\n')
match = list('abcdefghijklmnopqrstuvwxyz')

count2exact = 0
count3exact = 0

for box in input:
    counter = Counter(box)
    d = {c : counter.get(c,0) for c in match}

    for value in d.values():
        if value == 2:
            count2exact +=1
            break

    for value in d.values():
        if value == 3:
            count3exact +=1
            break

print(count2exact * count3exact)