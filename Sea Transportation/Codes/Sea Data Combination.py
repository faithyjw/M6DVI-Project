#software libraries
import pandas as pd
#import numpy as np

#loading the dataset
df1 = pd.read_csv('Sea Cargo Data.csv')
df2 = pd.read_csv('Cruise Ship Passengers Data.csv')

#combining both datasets together
#df2= left dataset, df1= right dataset
#axis= 1(vertical), 0 (horizontal)
df3= pd.concat ([df2, df1], axis =1)

#replacing any missing data
#df3 =df3.replace(np.nan,0)

#print the dataframe to see if it is correct
#print (df3)

#checking for any duplicates in the dataset
duplicates= df3.drop_duplicates(inplace=True)

#printing out the duplicates (if any)
print ("Df3:")
print(duplicates)
print("---------------------")

#checking of any missing value in its specific column
missing = pd.isnull(df3["Years"])
print(missing)

#output is a new CSV file
#header = first row, index =first coloum
df3.to_csv('Sea Transportation Data.csv', index=False)