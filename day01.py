


text_file = open("day01_input.txt", "r")
input = [int(n) for n in text_file.read().split('\n')]

text_file.close()

answer = 0

for _ in input:
    answer += _

print(answer)