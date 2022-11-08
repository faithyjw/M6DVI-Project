#software libraries
import pandas as pd
import numpy as np

#loading the dataset from an Excel Worksheet and accessing it via its respective sheet
df = pd.read_excel('Number of cruise ship passenger arrivals to Singapore from 2011 to 2020.xlsx', 
    sheet_name='Data')

#dropping the rows
df.drop(df.index[range(3,6)], axis=0, inplace=True)
df.drop([(2)], axis=0, inplace=True)

#removing the first empty column
del df[df.columns[0]]

#replacing the empty value with "Cruise Passenger Arrivals"
df= df.replace(np.nan,"Cruise Passenger Arrivals")

#replacing the title
df= df.replace('Number of cruise ship passenger arrivals Singapore 2011-2020', 'Years')

#inverting the "Year"/ "Number of Cruise Passengers" Column
df = df.iloc[::-1]
#checking if it's right
#print(df)
#to get the last row of the dataframe
df.iloc[8]
#setting last row to column name
df.columns = df.iloc[8]
#checking if it is correct
#print (df)

#adding "2021: 0" data into the dataset
#using index to access the rows to add another into the dataset
df.index = list(range(0)) + list(range(1, len(df) +1))
#setting the index to be the new value
df.loc[0] = [2021,0]
#sorting the index to be in acsending order
df = df.sort_index()
#checking if it is correct
# print(df)

#dropping the last row
df.drop(df.index[range(9,11)], axis=0, inplace=True)

#checking for any duplicates in the dataset
duplicates= df.drop_duplicates(inplace=True)

#printing out the duplicates (if any)
print ("Df:")
print(duplicates)
print("---------------------")

#checking of any missing value in its specific column
missing = pd.isnull(df["Years"])
print(missing)

#output is a new CSV file
#header = first row, index =first coloum
df.to_csv('Cruise Ship Passengers Data.csv', index=False)