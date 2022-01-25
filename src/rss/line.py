def drss_da(a, b, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += 2 * x * (a * x + b - y)
    return total


def drss_db(a, b, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += 2 * (a * x + b - y)
    return total


def rss(a, b, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += (a * x + b - y) ** 2
    return total


def rss_regression(a0, b0, dataset, learning_rate=0.1, iterations="rss"):
    a = a0
    b = b0
    if iterations == "rss":
        rssv = rss(a, b, dataset)
        while rssv > 0.6:
            rssv = rss(a, b, dataset)
            da = drss_da(a, b0, dataset)
            db = drss_db(a0, b, dataset)

            a = a - learning_rate * da
            b = b - learning_rate * db

    else:
        for i in range(iterations):
            da = drss_da(a, b, dataset)
            db = drss_db(a, b, dataset)

            a = a - learning_rate * da
            b = b - learning_rate * db
    # print(rss(a, b, dataset))
    # print([da, db])
    return [a, b]


# print(rss_regression(1, 0, [(0, 1), (2, 3), (3, 5)], 0.01))
