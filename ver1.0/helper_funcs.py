def sum_of_digits(num):
    """
    Calculates the sum of all digits in 'num'

    :param num: a positive natural number
    :return: an integer which stores the sum of digits
    """
    sum_ = sum(map(int, str(num)))
    return sum_


def make_one_digit(digit):
    """
    Implements an algorithm to return a single digit integer
    Doesn't keep the value of input 'digit' intact

    :param digit: takes in a positive number
    :return: the number itself; if its single digit
                else, converts to single digit and returns
    """
    while digit > 10:
        digit = sum_of_digits(digit)
    return digit


def neg_pos(iterlist):
    """
    Mutates the list by changing the sign of each other element

    :param iterlist: takes a list iterable
    :return: the mutated list
    """
    for i in range(1, len(iterlist), 2):
        iterlist[i] *= -1
    return iterlist
