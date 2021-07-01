###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


import pandas as pd


df1 = pd.read_csv('lecture12-pandas3/data1.csv')

# sample method to get a sample of data
# print(df1.sample(4)) 


# select columns fron a DataFrame
# print(df1[['City','OrderDate']]) 


# select columns and rows (index) fron a DataFrame
# print(df1[['City','OrderDate']][2:5]) 


# print(df1.index)
# df1.set_index('OrderId',inplace=True)
# print(df1.index)

# select by label
# print(df1.loc[33])

# select by index
# print(df1.iloc[5])

# select by label (from row with label 33 to the end)
# print(df1.loc[33:])


# print(df1.loc[33,['Quantity','UnitPrice']])




# drop columns from a DataFrame (returns a copy of DataFrame)
# dfDroppedColumns=df1.drop(columns=['Region','City'])
# print(dfDroppedColumns)


# drop columns from a DataFrame (in place)
# df1.drop(columns=['Region','City'],inplace=True)
# print(df1)



# Arrav of booleans to filter a DataFrame
print(df1['City']=='Boston')
print(df1[df1['City']=='Boston'])


# Arrav of booleans to filter a DataFrame (more complexity)
print((df1['City']=='Boston') & (df1['Product']=='Arrowroot'))
print(df1[(df1['City']=='Boston') & (df1['Product']=='Arrowroot')]) 



# filter a DataFrame with lambda function
print(df1[lambda row: row['City']=='Boston']) 





# filter a a DataFrame with filter-function
def filter_by_city(df):
    return (df['City']=='Boston') & (df.index>10)

print(df1[filter_by_city]) 