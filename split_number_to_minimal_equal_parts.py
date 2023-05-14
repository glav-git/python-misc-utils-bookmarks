def split_number_to_minimal_equal_parts(number: int, parts: int):
    """
    split_number_to_minimal_equal_parts(100, 2) -> [50, 50]
    split_number_to_minimal_equal_parts(100, 6) -> [17, 17, 17, 17, 16, 16]
    """
    one_part = number // parts
    l = [one_part] * parts
    if (rest := number % parts) != 0:
        l[:rest] = [one_part + 1] * rest
    return l
