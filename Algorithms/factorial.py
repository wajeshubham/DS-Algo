"""Normal method"""


def factorial(num):
    f = 1
    while num >= 1:
        f *= num
        num -= 1
    return f


"""using recursion"""


def factorial_rec(num):
    if num == 0:
        return 1
    return num * factorial_rec(num - 1)
