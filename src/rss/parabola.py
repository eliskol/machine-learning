def drss_da(a, b, c, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += 2 * (x ** 2) * (a * (x ** 2) + b * x + c - y)
    return total


def drss_db(a, b, c, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += 2 * x * (a * (x ** 2) + b * x + c - y)
    return total


def drss_dc(a, b, c, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += 2 * (a * (x ** 2) + b * x + c - y)
    return total


def rss(a, b, c, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += (a * (x ** 2) + b * x + c - y) ** 2
    return total


def rss_regression(a0, b0, c0, dataset, learning_rate=0.1, iterations="rss"):
    a, b, c = a0, b0, c0
    counter = 0

    if iterations == "rss":
        rss_value = rss(a, b, c, dataset)
        while rss_value > 0.8001:
            # print(rss_value)
            counter += 1
            print(counter)
            da = drss_da(a, b, c, dataset)
            db = drss_db(a, b, c, dataset)
            dc = drss_dc(a, b, c, dataset)

            a = a - learning_rate * da
            b = b - learning_rate * db
            c = c - learning_rate * dc

            rss_value = rss(a, b, c, dataset)

    else:
        for i in range(iterations):
            # rss_value = rss(a, b, c, dataset)
            da = drss_da(a, b, c, dataset)
            db = drss_db(a, b, c, dataset)
            dc = drss_dc(a, b, c, dataset)

            a = a - (learning_rate * da)
            b = b - (learning_rate * db)
            c = c - (learning_rate * dc)
    return [a, b, c]


# print(rss_regression(1, 0, 0, [(0, 2), (1, 0), (2, 1), (3, 1)], 0.008766))
# 869 iterations
