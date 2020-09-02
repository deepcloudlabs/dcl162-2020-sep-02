from functools import reduce
from itertools import accumulate
from operator import mul

numbers = [42, 16, 4, 8, 23, 15]
total = 0
for num in numbers:
    if num % 2 == 0:  # is even
        squared = num * num
        total = total + squared
print(total)

is_even = lambda n: print(f"is_even({n})") or n % 2 == 0
squared = lambda m: print(f"squared({m})") or m * m
add = lambda accum, n: print(f"add({accum},{n})") or accum + n
print(reduce(add, map(squared, filter(is_even, numbers)), 0))

print(reduce(add, numbers, 0))
print(reduce(mul, range(1, 10), 1))
fact = 1
for i in range(2, 10):
    fact = fact * i
print(fact)

numbers = [4, 8, 15, 16, 23, 42]
print(list(accumulate(numbers, add)))
