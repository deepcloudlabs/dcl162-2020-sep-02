import pandas as pd

df = pd.DataFrame([["TR1", "Jack Bauer", 100000],
                   ["TR2", "Kate Austen", 200000],
                   ["TR3", "Jin Kwon", 300000],
                   ["TR4", "Sun Kwon", 400000]], columns=["Iban", "Full Name", "Balance"])

df.to_csv('bank_accounts.csv')