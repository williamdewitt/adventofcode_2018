
text_file = open("day01_input.txt", "r")
input = [int(n) for n in text_file.read().split('\n')]
text_file.close()

answer = 0
answer_list = []
answer_list.append(0)
repeat_found = False
sum_found = False

while not sum_found or not repeat_found:
    for i, v in enumerate(input):
        answer += v

        if i == len(input) -1 and not sum_found:
            print(answer)
            sum_found = True
        
        if answer in answer_list and not repeat_found:
            print(answer)
            repeat_found = True

        answer_list.append(answer)
