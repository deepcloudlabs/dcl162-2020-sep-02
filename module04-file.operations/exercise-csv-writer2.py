import csv

bank_accounts = [["TR1", "Jack Bauer", 100000],
            ["TR2", "Kate Austen", 200000],
            ["TR3", "Jin Kwon", 300000],
            ["TR4", "Sun Kwon", 400000]]

with open('accounts2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(bank_accounts)