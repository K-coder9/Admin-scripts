import pandas as pd
import openpyxl
import os 
import csv 

member_list = input("What is the name of the members file?")
list = str(member_list)+'.csv'

df = pd.read_csv(list)


length = len(df)+1
print(length)
#include for loop that counts up to 8 of all rows and starts counting again after 8
#saves each interation into a new data frame then upload it into a python file
j=0
# for i in range(0,length):
#while loop for as long as j+5 is less than length
while j < length:
    #df1= df.iloc[j:j+8]
    df1= df.iloc[j:j+8]
    file_name = str(j)
    extension = '.csv'
    df1.to_csv(file_name+extension,index = False)

    j=j+8
    # with open(file_name+extension,'w') as file:
    #     file.write('')
#how to get rid of index column 
#num = num+5
#can I include a variable in the name like the number of file 
#upload dataframe into new file with index name 

