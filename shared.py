def return_lines_as_list(file):
    """

    :rtype: list of str
    """
    # read lines
    lines = file.readlines()

    def strip(string):
        """
        Removes whitespace from beginning and end of string
        :type string: str
        """
        return string.strip()

    # Coverts our lines to list
    return list(map(strip, lines))
