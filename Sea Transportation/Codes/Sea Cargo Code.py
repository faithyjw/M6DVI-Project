#software library
import pandas as pd

#loading the dataset
df = pd.read_csv('Sea Cargo And Shipping Statistics.csv')

#print the dataframe
#print(df)

#print dataframe shape
#print(df.shape)

#dropping the first few rows
df.drop(df.index[range(0,7)], axis=0, inplace=True) #axis 1 = column, axis 0 = row
#dropping the last few rows
df.drop(df.index[range(10,56)], axis=0, inplace=True)

#checking if the drop was correct
#print(df)
#print (df.shape)

#handling missing values
#dataset was manually keyed in "na", so fillna() can't be used
df= df.replace('na', '0')

#replacing the titles
df= df.replace('Total Cargo (Thousand Tonnes)', 'Total Cargo')

df= df.replace('Total Container Throughput (Thousand Twenty-Foot Equivalent Units)', 'Total Container Throughput')

df= df.replace('Bunker Sales (Thousand Tonnes)', 'Bunker Sales')

#to get the first row the dataframe
#first_row=df.iloc[0]
#print(first_row)
#setting first row to column name
df.columns = df.iloc[0]
#to check if it is correct
#print (df)

#printing the columns name
#for col in df.columns:
#    print(df.columns)

#dropping the columns that I do not need
df= df.drop(columns=['Total Cargo -> Cargo (General) (Thousand Tonnes)',
    'Total Cargo -> Cargo (Bulk) (Thousand Tonnes)',
    'Data Series',
    'Singapore Registry Of Ships (End Of Period) - Number (Number)', 
    'Singapore Registry Of Ships (End Of Period) - 000 GT (Thousand Gross Tonnes)'])
#check if the dropping is correct
print(df)

#checking of any missing value in its specific column
#missing = pd.isnull(df[""])
#print(missing)

#output is a new CSV file
#header = first row, index =first coloum
df.to_csv('Sea Cargo Data.csv', index=False, header=None)