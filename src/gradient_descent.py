def minimize(fprime, x0, learning_rate=0.001, num_iterations=1000):
    x_old = x0
    for i in range(num_iterations):
        x_old = x_old - (learning_rate * fprime(x_old))
    return x_old
