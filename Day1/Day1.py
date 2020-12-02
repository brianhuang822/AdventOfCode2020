# Opens file and set to file variable
with open('input.txt') as file:
    # read lines
    lines = file.readlines()
    def strip(str):
        """
        Removes whitespace from beginning and end of string
        :type str: str
        """
        return str.strip()
    # Coverts our lines to list
    lines_stripped = list(map (strip, lines))
    # Avoid the case of 1010 where it will think it is in the set again even if there's only 1 entry
    # By doing a map and then subtracting, we get an O(n) solution instead of the naive O(n^2)
    lines_count_map = {}
    # Go through every number and make a counter for it
    for number in lines_stripped:
        number = int(number)
        if number not in lines_count_map:
            lines_count_map[number] = 0
        lines_count_map[number] += 1
    # Now for every key, we check if theres a corresponding key meeting our condition of 2020-key,
    # if so that is our answer
    for key in lines_count_map:
        possible_other_key = (2020 - key)
        if possible_other_key in lines_count_map:
            if (key == possible_other_key and lines_count_map[key] >= 2) or key != possible_other_key:
                print(key * possible_other_key)
                break
    #part 2 we do the same thing, but more checks against cases of keys equalling to each other
    for key in lines_count_map:
        remaining = 2020 - key
        for key2 in lines_count_map:
            key3 = remaining - key2
            if key3 in lines_count_map:
                # If they're all the same, we need to make sure they have a count of 3
                if key == key2 == key3:
                    if lines_count_map[key] >= 3:
                        print(key*key2*key3)
                        exit(0)
                elif key == key2 or key == key3:
                    if lines_count_map[key] >= 2:
                        print(key*key2*key3)
                        exit(0)
                elif key2 == key3:
                    if lines_count_map[key2] >= 2:
                        print(key*key2*key3)
                        exit(0)
                # no keys are the same
                else:
                    print(key * key2 * key3)
                    exit(0)



