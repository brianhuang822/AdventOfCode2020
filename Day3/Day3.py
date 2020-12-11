import shared


def count_trees(lines, right=1, down=1):
    current_pos = 0
    counter = 0
    # range 0..lines, skipping # down
    for i in range(0, len(lines), down):
        line = lines[i]
        # modulo makes line extend to infinity
        if line[current_pos % len(line)] == "#":
            counter += 1
        current_pos += right
    return counter


with open('input.txt') as file:
    lines_stripped = shared.return_lines_as_list(file)
    # Part 1
    print(count_trees(lines_stripped, right=3, down=1))
    # Part 2
    print(count_trees(lines_stripped, right=1, down=1)
          * count_trees(lines_stripped, right=3, down=1)
          * count_trees(lines_stripped, right=5, down=1)
          * count_trees(lines_stripped, right=7, down=1)
          * count_trees(lines_stripped, right=1, down=2))
