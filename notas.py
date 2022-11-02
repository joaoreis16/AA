global iterations_counter


def f1(n):
    iterations_counter = 0

    r = 0
    for i in range(n + 1): 
        r += i
        iterations_counter += 1

    return r


def f2(n):
    r = 0
    for i in range(n + 1):
        for j in range(n + 1):
            r += 1

            iterations_counter += 1

    return r


def f3(n):
    r = 0
    for i in range(n + 1):
        for j in range(n + 1):
            r += 1

            iterations_counter += 1

    return r

print(f1(10))