#Ikram's part    

# 1 display the content of the spreadsheet Using Pandas

import pandas as pd

with open('sales2.csv', 'r') as sales_file:
        data = pd.read_csv('sales2.csv')
print(data)

# 2 Import data from  specific columns using pandas

df = pd.read_csv('sales2.csv')
print("Sales""\n",df["sales"])
print('Expenditure''\n',df["expenditure"])     
       
# 3 calculating the sum of sales without importing the data from the csv file

sales = [6226, 1521,  1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812]
total = sum(sales)
output= " The total of the sales in the year 2018 is €" + str(total)

print(output)      
      
# 4 getting the percentages of each month's sales

df = pd.read_csv('sales2.csv')

df['Percentage'] = df['sales'] * 100/df['sales'].sum()

print('sales\' %''\n',df['Percentage'])
     
          
#Anna's part    
    
import csv

def read_data():
    #1  
    data = []
    with open('sales.csv','r') as sales_csv:
           spreadsheet = csv.DictReader(sales_csv, delimiter='\t')
            for row in spreadsheet:
                data.append(row)
    #2
    return data     
#3
def run():
    data=read_data()
    sales=[]
    for row in data:
        sale = int(row['  sales'])
        sales.append(sale)

    total=sum(sales)
    print('Total sales:{}'.format(total))

run()      
import csv
with open('sales.csv', 'r') as sales_file:
        content = sales_file.read()
print(content)
data=[] 
with open('sales.csv','r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv, delimiter='\t')
    for row in spreadsheet:
        data.append(row)
                                            
sales=[]    
for row in data:
    sale = int(row['  sales'])
    sales.append(sale)

          
total = sum(sales)
print("The total of all sales is: €",total)     
average=sum(sales) / len(sales)
print('The average is', average)

maximum_sales=max(sales)
print('The maximum sales number is', maximum_sales)

minimum_sales=min(sales)
print('The minimum sales number is', minimum_sales)
