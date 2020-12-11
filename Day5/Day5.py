import shared
import math


def get_seat(line):
    f, b, l, r = 0, 127, 0, 7
    for char in line:
        if char == "F":
            b = (f + b) // 2
        elif char == "B":
            f = (f + b) // 2
        elif char == "L":
            r = (r + l) // 2
        elif char == "R":
            l = (r + l) // 2
    return b, r


with open('input.txt') as file:
    lines_stripped = shared.return_lines_as_list(file)
    seats = {}
    highest = 0
    seats_taken_set = set()
    starting_seat = math.inf
    ending_seat = -math.inf
    for line in lines_stripped:
        seats[line] = get_seat(line)
        seat_id = seats[line][0] * 8 + seats[line][1]
        highest = max(highest, seat_id)
        starting_seat = min(seats[line][0], starting_seat)
        ending_seat = max(seats[line][0], ending_seat)
        seats_taken_set.add(seat_id)
    # part 1
    print(highest)
    # part 2
    for i in range(starting_seat + 1, ending_seat):
        for j in range(0, 8):
            seat = (i * 8 + j)
            if seat not in seats_taken_set:
                print(seat)
                exit(0)
