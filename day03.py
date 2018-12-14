import operator
import re

# Part 1
claims = []
id_reg = r"\d*\b\s"
rec_reg = r"\d*,\d*"
inch_reg = r"\d*x\d*"

claim_id = 0
rect = (0,0)
size = (0,0)

w, h = 1000, 1000
squares = [[0 for x in range(w)] for y in range(h)] 

with open("day03_input.txt", "r") as f:
    for line in f:
        claims.append(line)

    for record in claims:
        claim_id = re.search(id_reg, record).group(0)
        rect = re.search(rec_reg, record).group(0).split(",")
        size = re.search(inch_reg, record).group(0).split("x")

        print("{} {} {}".format(claim_id, rect, size))

        squares[rect[0]][rect[1]] = squares[rect[0]][rect[1]] + 1



#print(claims)

# Part 2
