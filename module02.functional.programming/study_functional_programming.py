class Account:
    pass


name = "Jack"
number = 42
numbers = [4, 8, 15, 16, 23, 42]
acc = Account()
is_odd = lambda n: n % 2 == 0
print(name)
print(number)
print(is_odd(42))

names = ["jack", "james", "ben", "sun", "jin", "kate"]
print(names)
names.sort()  # mutates list
print(names)

names = ["jack", "james", "ben", "Sun", "jin", "kate", "binnur"]
names_sorted = sorted(names, reverse=True)  # do not mutates list
print(names)
print(names_sorted)

identity = lambda s: s
order_by_length = lambda s: len(s)
order_by_lowercase = lambda s: s.lower()
names.sort(key=order_by_lowercase)
print(names)

countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80000000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67000000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60000000}
]
european_countries = []
for country in countries: # external loop
    if country['continent'] == 'europe':
        european_countries.append(country)
european_countries = sorted(european_countries, key=lambda country: country['population'], reverse=True)
print(european_countries)

# filter-map-reduce
european = lambda country: country['continent'] == 'europe'
country_name6 = lambda country: len(country['name']) == 6
order_by_population = lambda country: country['population']
print(sorted(list(filter(country_name6, countries)), key=order_by_population, reverse=True)) # one liner, internal loop