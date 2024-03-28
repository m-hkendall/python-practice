#Introduction to data analysis. Following along with "Python for Geographic Data Analysis" (https://pythongis.org/part1/chapter-03/nb/00-pandas-basics.html)

#Two-dimensional, table-like data sequences are stored in two-dimensional DataFrames (objects with labeled rows and columns).
#One-dimensional data sequences are stored in one-dimensional Series - therefore, one row or one column in a pandas DataFrame is a pandas Series. 

import pandas as pd

db = pd.read_csv("C:\\Users\\maddy\\OneDrive\\Documents\\Github\\python-geospatial-practice\\data\\NFDB_point_20220901.csv", usecols=['FID', 'LATITUDE', 'LONGITUDE', 'YEAR', 'MONTH', 'DAY', 'SIZE_HA', 'CAUSE', 'ECOZ_NAME'])

print(db.head())
print(len(db)) #Returns the number of records
print(db.shape) #.shape returns a tuple with the number of rows as the first element and the number of columns as the second element
print(db.columns.values) #.columns.values returns an index object that contains the column labels
print(db.index) #Returns information about the row identifiers
print(db.dtypes) #Check the data type of all columns
print(len(db.columns)) #This finds the number of columns

selection = db[['FID', 'SIZE_HA']] #Selecting columns
print(selection.head())
print(type(selection)) #This selection is still a data frame that can use all the methods and attributes related to a data frame

print(type(db['FID'])) #Proof that one column from a data frame is a seris

print(db['LATITUDE'].unique()) #This returns all the unique values from the specified column
print('There were', db['LATITUDE'].nunique(), 'fires with unique latitudes') #.nunique() returns the number of unique values in the specified column

print(db.describe()) #.describe() returns the summary statistics for each column

number_series = pd.Series([4,5,6,7], index=['a','b','c','d']) #create a pandas Series from a list, along with a custom index
print(number_series)

fids = [1,2,3,4]
latitudes = [49,50,51,52]
longitudes = [121,122,123,124]

new_data = pd.DataFrame(data={'FID': fids, 'LAT': latitudes, 'LON': longitudes})
print(new_data.head())