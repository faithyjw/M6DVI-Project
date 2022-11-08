#software library
import pandas as pd

#loading the dataset
df = pd.read_csv('Civil Aircraft Arrivals And Departures, Passengers And Mail - Changi Airport.csv')

#print the dataframe
#print(df)

#print dataframe shape
#print(df.shape)

#dropping the first few rows
#axis 1 = column, axis 0 = row
df.drop(df.index[range(0,8)], axis=0, inplace=True)
#dropping the last few rows
df.drop(df.index[range(10, 78)], axis=0, inplace=True)

#checking to see if the drop was correct
#print(df)

#replacing the titles
df= df.replace('Data Series', 'Years')

df = df.replace('Total Aircraft Arrivals And Departures -> Aircraft Arrivals (Number)', 'Aircraft Arrivals')

df= df.replace('Total Passengers -> Passengers Arriving (Number)', 'Passengers Arriving')

df= df.replace('Total Passengers -> Passengers In Transit (Number)', 'Passengers In Transit')

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
df= df.drop(columns=['Total Aircraft Arrivals And Departures (Number)', 
    'Total Aircraft Arrivals And Departures -> Aircraft Departures (Number)',  
    'Total Passengers -> Passengers Departing (Number)',
    'Total Mail -> In-Coming Mail (Tonne)',
    'Total Mail -> Out-Going Mail (Tonne)',
    'Total Passengers (Number)'])
#checking to see if the dropping is correct
#print(df)

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
df.to_csv('Civil Aircraft, Passengers and Mail Data.csv', index=False, header=None)