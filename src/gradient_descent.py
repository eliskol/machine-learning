def minimize(fprime, x0, learning_rate=0.001, num_iterations=1000):
    x_old = x0
    for i in range(num_iterations):
        x_old = x_old - (learning_rate * fprime(x_old))
    return x_old


def multivar_minimize(gradient, v0, learning_rate=0.001, num_iterations=1000):
    v_old = v0
    for i in range(0, num_iterations):
        for j, coord in enumerate(v_old):
            v_old[j] = coord - learning_rate * gradient(v_old)[j]
    return v_old
