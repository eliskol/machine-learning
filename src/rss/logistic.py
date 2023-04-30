from math import e


def drss_da(a, b, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += (-2 * x * (e ** (a * x + b))) / ((1 + (e ** (a * x + b))) ** 3) + (
            2 * x * y * e ** (a * x + b)
        ) / ((1 + e ** (a * x + b)) ** 2)
    return total


def drss_db(a, b, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += (-2 * (e ** (a * x + b))) / ((1 + (e ** (a * x + b))) ** 3) + (
            2 * y * e ** (a * x + b)
        ) / ((1 + e ** (a * x + b)) ** 2)
    return total


def rss(a, b, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += (((1 / (1 + e ** (a * x + b)))) - y) ** 2
    return total


def regression(a0, b0, dataset, learning_rate=0.01, iterations="auto"):
    a, b = a0, b0
    if iterations == "auto":
        rss_value = rss(a, b, dataset)
        while rss_value > 0.05:
            da = drss_da(a, b, dataset)
            db = drss_db(a, b, dataset)

            a = a - learning_rate * da
            b = b - learning_rate * db

            rss_value = rss(a, b, dataset)
            print(rss_value)

    else:
        for i in range(iterations):
            da = drss_da(a, b, dataset)
            db = drss_db(a, b, dataset)

            a = a - learning_rate * da
            b = b - learning_rate * db

    return [b, a]
