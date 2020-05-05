import pandas as pd
import numpy as np

csv_path = "budget_data.csv"
bank_df = pd.read_csv(csv_path)
bank_df.head(10)

total_months = len(bank_df)

total_pl = bank_df["Profit/Losses"].sum()

mean_pl = bank_df["Profit/Losses"].mean()

max_profit = bank_df["Profit/Losses"].max()
max_profit_loc = bank_df.loc[bank_df["Profit/Losses"] == max_profit]

min_profit = bank_df["Profit/Losses"].min()
min_profit_loc = bank_df.loc[bank_df["Profit/Losses"] == min_profit]

print("Financial Analysis")
print("-----------------------------")
print("Total Months: ",total_months)

# how do I format this as a currency?
print("Total: ",total_pl)
print("Average Change: ",mean_pl)

# how do I remove the column labels? 
print("Greatest Increase in Profits: ",max_profit_loc)
print("Greatest Decrease in Profits: ",min_profit_loc)