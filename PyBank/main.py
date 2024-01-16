# assign variables
change_count = 0
months_sum = 0
profit_sum = 0
loss_sum = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""



import csv

#set file path
budget_data_csv = ("Resources/budget_data.csv")

#open file
with open(budget_data_csv) as csv_file:
    budget = csv.reader(csv_file) 

        #read header row, skip move through column B
    header = next(budget)
    
    January_list = next(budget)
    
    profit_sum = profit_sum + int(January_list[1])
    months_sum += 1
    previous_profit = int(January_list[1])

#calculate net total amount of profit/losses for the entire period created with tutor David Chao
    for row in budget:
        profit_sum = profit_sum + int(row[1])
        months_sum += 1

        current_profit = int(row[1])
        change = current_profit - previous_profit
        total_change = total_change + change
        change_count += 1

        previous_profit = current_profit

#changes in profit/losses for entire period created with tutor David Chao
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0]

#greatest decrease in profits(date and amount) over the entire period      
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[1]

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[1]
         
#print output f statement created with tutor David Chao
output = f"""   
Financial Analysis
----------------------------
Total Months: {months_sum}
Total: ${profit_sum:,}
Average Change: ${total_change/change_count:.2f}
Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase:,}
Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease:,}
"""

print(output)

#save to file
with open("Analysis/budget_analysis.txt", "w") as outfile:
    outfile.write(output)
