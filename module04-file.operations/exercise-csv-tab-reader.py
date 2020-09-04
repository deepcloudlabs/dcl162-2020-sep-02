import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)
