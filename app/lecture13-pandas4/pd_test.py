###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


import pandas as pd


df1 = pd.read_csv('lecture13-pandas4/data1NotClean.csv')
# print(df1.to_string())




# find rows with empty cell in a Frame
# print(df1.isna())
# print(df1.isna().any())
# print(df1.isna().any(axis=1))
# print(df1[df1.isna().any(axis=1)])





# drop rows with empty cell
# print(df1.dropna().to_string()) 




# drop rows with empty cell on the City column
# print(df1.dropna(subset=['City']))




# dropna make a copy from original DataFrame
# df1.dropna()
# print(df1.to_string()) 
# df2=df1.dropna()
# print(df2.to_string()) 



# df1.dropna(inplace = True)
# print(df1.to_string()) 



# df1.fillna('Hi!!!!!',inplace=True)
# print(df1.to_string()) 



# df1['City'].fillna('Tehran',inplace=True)
# print(df1.to_string()) 



# df1['Quantity'].fillna(df1['Quantity'].mean(),inplace=True)
# df1['Quantity'].fillna(df1['Quantity'].median(),inplace=True)
# print(df1.to_string()) 


# show and remove duplicate rows
print(df1.duplicated())
df1.drop_duplicates(inplace = True)
print(df1.to_string())
