def gen_even(n: int):
    for x in range(0, n + 1, 2):
        yield x


def gen_fib_upto(n: int):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
