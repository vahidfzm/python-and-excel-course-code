###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


import pandas as pd


# read as DataFrame from excel-file
# df1 = pd.read_excel('lecture11-pandas2/data1.xlsx')
# print(df1.to_string()) 



# read as DataFrame from csv-file
# df2 = pd.read_csv('lecture11-pandas2/data2.csv')
# print(df2.to_string()) 




# read as DataFrame from csv-file with setting delimiter
# df3 = pd.read_csv('lecture11-pandas2/data3.csv', delimiter=";")
# print(df3.to_string()) 




# read as DataFrame from json-file
# df4 = pd.read_json('lecture11-pandas2/data4.json')
# print(df4.to_string()) 





# read as DataFrame from txt-file
# df5 = pd.read_csv('lecture11-pandas2/data5.txt', delimiter="\t")
# print(df5.to_string()) 




# read as DataFrame from csv-file without header
# df6 = pd.read_csv('lecture11-pandas2/data6.csv',header=None)
# df6.columns=["OrderDate","Region","City","Category","Product","Quantity","UnitPrice","TotalPrice"]
# print(df6.to_string()) 




df2=pd.read_csv('lecture11-pandas2/data2.csv')
# print(df2.head())
# print(df2.tail())
# print(df2.info())
# print(df2['City'])
# print(df2.loc[2])
# print(df2.loc[[2,5]])
print(df2.loc[2:5])

newDataFrame=df2.loc[2:5]
newDataFrame.to_excel('newDataFrame.xlsx')