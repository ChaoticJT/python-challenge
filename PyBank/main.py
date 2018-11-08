#modules
import csv
import os

#CSV and Reader
RawBudgetData= os.path.join("Resources", "budget_data.csv")
BudgetAnalysis = os.path.join("analysis", "budget_analysis.txt")
with open(RawBudgetData) as BudgetData:

#Parameters
TotalMonths = 0
NetTotal = 0
MonthChange_list = []
NetChange_list = []
GreatestInc = ["", 0]
GreatestDec = ["", 9999999999]


Bud_reader = csv.reader(BudgetData)
#Setting Reader
    header = next(Bud_reader)
    FirstRow = next(Bud_reader)
    TotalMonths = TotalMonths + 1
    NetTotal = NetTotal + int(FirstRow,[1])
    prevNet = int(FirstRow, [1])

for row in Bud_reader:
#Totals
    TotalMonths = TotalMonths + 1
    NetTotal = NetTotal + int(FirstRow,[1])

# Change
    NetChange = int(row[1]) - prevNet
    prevNet = int(row[1])
    NetChange_list = NetChange_list + [NetChange]
    MonthChange = MonthChange + [row[0]]

#Increase
       if NetChange > GreatestIncrease[1]:
            GreatestInc[0] = row[0]
            GreatestInc[1] = NetChange
#Decrease
       if NetChange > GreatestDec[1]:
            GreatestDec[0] = row[0]
            GreatestDec[1] = NetChange
#Average Net Change
NetAvg = sum(NetChange_list) / len(NetChange_list)

#Output
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(output)

with open(BudgetAnalysis, "w") as txt_file:
    txt_file.write(output)
