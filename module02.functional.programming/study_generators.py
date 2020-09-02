def sequence(n):
    while n > 1:
        print(f"sequence: {n}")
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


def squared(numbers):
    for number in numbers:
        print(f"squared: {number}")
        yield number * number


total = 0
for num in squared(sequence(7)):  # pipeline
    total = total + num
    print(f"total: {total}")
