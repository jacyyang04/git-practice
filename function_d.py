def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """



    result = None
    for number in numbers:
        if result == None or result < number:
            result = number
    return result


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
