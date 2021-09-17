def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
max = 0
for each in numbers:
    if each > max:
        max = each
    return max




if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
