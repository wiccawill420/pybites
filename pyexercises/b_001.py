def sum_numbers(numbers=None):
    try:
        x = len(numbers)
    except TypeError:
        return sum(range(1,101))
    if x == 0:
        return 0
    return sum(list(numbers))
