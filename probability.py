from fraction import Frac
import random


def rand_prob(precision):
    exp = 10 ** precision
    p = 0
    while p == 0 or p == exp:
        p = random.randrange(0, exp)
    return Frac(p, exp)


def rand_unique_table(size, start, stop):
    result = []
    for i in range(0, size):
        while True:
            value = random.randrange(start, stop)
            if value not in result:
                result.append(value)
                break

    result.sort()
    return result


def rand_prob_table(size, precision):
    exp = 10 ** precision
    points = [0]
    result = []

    for i in range(0, size - 1):
        p = random.randrange(0, exp)
        while p in points:
            p = random.randrange(0, exp)
        points.append(p)
    points.sort()

    points.append(exp)
    for i in range(len(points)):
        points[i] = Frac(points[i], exp)

    for i in range(1, size + 1):
        result.append(points[i] - points[i - 1])

    return result, points
