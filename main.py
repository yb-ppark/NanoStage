def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_sum(n):
    return sum(fibonacci(n))


def fibonacci_average(n):
    if n <= 0:
        return 0
    return fibonacci_sum(n) / n


if __name__ == "__main__":
    n = 10
    fib_list = list(fibonacci(n))
    print(f"Fibonacci({n}): {fib_list}")
    print(f"Sum: {fibonacci_sum(n)}")
    print(f"Average: {fibonacci_average(n):.2f}")
