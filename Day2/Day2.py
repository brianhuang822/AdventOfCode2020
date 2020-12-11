import shared

with open('input.txt') as file:
    lines_stripped = shared.return_lines_as_list(file)
    valid_passwords = 0
    valid_passwords_part_two = 0
    for line in lines_stripped:
        # parsing each line
        # low, high is the range
        # letter_policy is the letter we're gonna check
        # password = password :)
        policy, password = line.split(':')
        password = password.strip()
        num_chars, letter_policy = policy.split(' ')
        low, high = num_chars.split("-")
        low = int(low)
        high = int(high)
        letter_policy = letter_policy.strip()[0]
        if low <= password.count(letter_policy) <= high:
            valid_passwords += 1
        if (password[low - 1] == letter_policy) != (password[high - 1] == letter_policy):
            valid_passwords_part_two += 1
    print(valid_passwords)
    print(valid_passwords_part_two)
