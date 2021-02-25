def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n-1)


if __name__=="__main__":
    print(fib(20))
    print(factorial(0))



