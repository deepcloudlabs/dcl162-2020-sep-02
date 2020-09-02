numbers = [5, 9, 15, 17, 23, 43]

result = False
for num in numbers:
    if num % 2 == 0:
        result = True
        break
print(result)
is_even = lambda n : n % 2 == 0
is_odd = lambda n : n % 2 == 1
is_there_any_even_number = any(map(is_even, numbers))
print(is_there_any_even_number)
is_there_any_odd_number = any(map(is_odd, numbers))
print(is_there_any_odd_number)
all_number_odd = all(map(is_odd, numbers))
print(all_number_odd)