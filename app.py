import random
def main():
    x = 10
    # y = random.randint(1, 5)
    y = random.randint(1,2)

    xy = x * y

    xy_2 = xy ** 2

    return xy_2


#
#
#
#


def multiplication(x, y):
    return x * y

def square(x):
    return x ** 2


def main2_testable():
    x = 10
    # y = random.randint(1,2)
    y = 2

    xy = multiplication(x, y)

    xy_2 = square(x)

    xy_2 = xy ** 2

    return xy_2