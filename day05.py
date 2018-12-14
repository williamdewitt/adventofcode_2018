test_string = "dabAcCaCBAcCcaDA"
polymers = "abcdefghijklmnopqrstuvwxyz"

with open("day05_input.txt", "r") as f:
    test_string = f.read()

def react(poly_length):
    reaction = True

    while reaction:
        reaction = False

        for i in range(0, len(poly_length)):
            if i < len(poly_length) -1:
                if poly_length[i].lower() == poly_length[i+1].lower():
                    if poly_length[i].islower() and not poly_length[i+1].islower() or poly_length[i].isupper() and not poly_length[i+1].isupper():
                        del poly_length[i+1]
                        del poly_length[i]
                        reaction = True

    return len(poly_length)

chars = list(test_string)
shortest = len(chars)
print(len(chars))

for i in list(polymers):
    test = test_string.replace(i.lower(), "")
    test = test.replace(i.upper(), "")
    test_arr = list(test)

    react_len = react(test_arr)
    
    if react_len < shortest:
        shortest = react_len

print(shortest)