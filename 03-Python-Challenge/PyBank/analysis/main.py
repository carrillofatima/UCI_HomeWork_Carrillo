#Import OS and CSV files
import os   
import csv

#Set Path for CSV File
csv_path = os.path.join("..","Resources","budget_data.csv")


#Read the CSV file   
with open(csv_path) as csv_file: 
      
    csv_reader = csv.reader(csv_file, delimiter= ',')
    csv_header = next(csv_file)
    #print(csv_reader)   

#Declare variables

    Months = []
    Profit_Loss = []
    Changes_profit_loss = []
    Greatest_Increase = ""
    Greatest_Decrease = ""
 
#Count total number of months the data encapsulates
    for row in csv_reader:
        Months.append(row[0])   
        Profit_Loss.append(int(row[1]))

#Print Statements
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", len(Months))
    print("Net Total: $", sum(Profit_Loss))

    for i in range(1, len(Profit_Loss)):
        
#Average change between months
        Changes_profit_loss.append(Profit_Loss[i] - Profit_Loss[i-1])
#Find average of values
        Average_Change = sum(Changes_profit_loss) / len(Changes_profit_loss)
        
        # Determine greatest increase and date
        Greatest_Increase = max(Changes_profit_loss)
        Greatest_Increase_Date = str(Months[Changes_profit_loss.index(max(Changes_profit_loss))])
        
        
#Determine greatest decrease and date
        Greatest_Decrease = min(Changes_profit_loss)
        Greatest_Decrease_Date = str(Months[Changes_profit_loss.index(min(Changes_profit_loss))])
        
#Print Statements
    print("Average Change: $", round(float(Average_Change),2))
    print("Greatest Increase: ", Greatest_Increase_Date, "($", Greatest_Increase,")")
    print("Greatest Decrease: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")")        

#Text File
txt_path = os.path.join("PyBank.txt")

with open("txt_path.txt", "w") as PyBank_file: 

    PyBank_file.write(f'Financial Analysis\n')
    PyBank_file.write(f'-------------------------------\n')
    PyBank_file.write(f'Total Months: {len(Months)}\n')
    PyBank_file.write(f'Net Total: $ {sum(Profit_Loss)}\n')
    PyBank_file.write(f'Average Change: $ {round(float(Average_Change),2)}\n')  
    PyBank_file.write(f'Greatest Increase: {Greatest_Increase_Date} (${Greatest_Increase})\n')
    PyBank_file.write(f'Greatest Decrease: {Greatest_Decrease_Date} (${Greatest_Decrease})\n')
    PyBank_file.close()













