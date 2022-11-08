#software library
import pandas as pd

#loading the dataset
df = pd.read_csv('Public Transport Operation And Ridership.csv')

#print the dataframe
#print(df)

#print dataframe shape
#print(df.shape)

#dropping the first few rows
#axis 1 = column, axis 0 = row
df.drop(df.index[range(0,8)], axis=0, inplace=True)
#dropping the last few rows
df.drop(df.index[range(10,37)], axis=0, inplace=True)

#checking if the drop was correct
#print(df)
#print (df.shape)

#handling missing values
#dataset was manually keyed in "na", so fillna() can't be used
df= df.replace('na', '0')

#replacing the titles
df= df.replace('Data Series', 'Years')

df= df.replace('Average Daily Ridership - MRT (Thousand Passenger-Trips)', 'MRT Passengers')

df= df.replace('Average Daily Ridership - LRT (Thousand Passenger-Trips)', 'LRT Passengers')

df= df.replace('Average Daily Ridership - Bus (Thousand Passenger-Trips)', 'Bus Passengers')

df= df.replace('Average Daily Trip - Point-To-Point (P2P) Transport (Taxis And Private Hire Cars) (Thousand Daily-Trips)',
    'Taxis & Private Hirers Passengers')

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
df= df.drop(columns=['Rail Length (Kilometres)',
    'Rail Length -> Mass Rapid Transit (MRT) (Kilometres)',
    'MRT km Operated (Thousand Train-Kilometres)',
    'LRT km Operated (Thousand Car-Kilometres)', 
    'Rail Length -> Light Rail Transit (LRT) (Kilometres)'])
#check if the dropping is correct
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
df.to_csv('Land Transportion Data.csv', index=False, header=None)