import shared
import re

with open('input.txt') as file:
    lines_stripped = shared.return_lines_as_list(file)
    passports = []
    required_keys = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"]

    other_keys = ["cid"]
    current_passport = {}
    for line in lines_stripped:
        if line == "":
            passports.append(current_passport)
            current_passport = {}
        else:
            for pairs in line.split():
                key, value = pairs.split(":")
                current_passport[key] = value

    passports.append(current_passport)
    valid_passport = 0
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for passport in passports:
        if not all([key in passport for key in required_keys]):
            continue
        conditions = [
            1920 <= int(passport["byr"]) <= 2002,
            2010 <= int(passport["iyr"]) <= 2020,
            2020 <= int(passport["eyr"]) <= 2030,
            any([passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76,
                 passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193]),
            len(re.findall(r'^#[0-9a-f]{6}$', passport["hcl"])) == 1,
            passport["ecl"] in valid_eye_colors,
            len(re.findall(r'^[0-9]{9}$', passport["pid"])) == 1,
        ]
        if all(conditions):
            valid_passport += 1

    # Part 1 & 2
    print(valid_passport)
