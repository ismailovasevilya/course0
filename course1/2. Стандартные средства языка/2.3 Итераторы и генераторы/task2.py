def primes():
    x = 2
    while True:
        result = [x % i == 0 for i in range (2, x)]
        if not any(result):
            yield x
        x += 1
