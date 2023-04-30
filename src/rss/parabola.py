def drss_da(a, b, c, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += 2 * (x**2) * (a * (x**2) + b * x + c - y)
    return total


def drss_db(a, b, c, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += 2 * x * (a * (x**2) + b * x + c - y)
    return total


def drss_dc(a, b, c, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += 2 * (a * (x**2) + b * x + c - y)
    return total


def rss(a, b, c, dataset):
    total = 0
    for point in dataset:
        x, y = point[0], point[1]
        total += (a * (x**2) + b * x + c - y) ** 2
    return total


def rss_regression(a0, b0, c0, dataset, learning_rate=0.1, iterations="auto"):
    a, b, c = a0, b0, c0

    if iterations == "auto":
        rss_value = rss(a, b, c, dataset)
        while rss_value > 0.8001:
            da = drss_da(a, b, c, dataset)
            db = drss_db(a, b, c, dataset)
            dc = drss_dc(a, b, c, dataset)

            a = a - learning_rate * da
            b = b - learning_rate * db
            c = c - learning_rate * dc

            rss_value = rss(a, b, c, dataset)

    else:
        for i in range(iterations):
            da = drss_da(a, b, c, dataset)
            db = drss_db(a, b, c, dataset)
            dc = drss_dc(a, b, c, dataset)

            a = a - (learning_rate * da)
            b = b - (learning_rate * db)
            c = c - (learning_rate * dc)
    return [a, b, c]
