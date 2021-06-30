###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


import pandas as pd


# create a simple DataFrame 
myDataset = {
  'product': ["White Paper", "Marker", "Envelope"],
  'price': [12.60,4.70,1.20]
}
myDataframe = pd.DataFrame(myDataset)
print(myDataframe)
print(myDataframe['product'])





# create Series from a list
myList = [3,6,67,45]
mySeries = pd.Series(myList)
print(mySeries)
print(mySeries[0])





# create Series (with label) from a list
myList = [3,6,67,45]
myLabels=["a","b","c","d"]
mySeriesWithLabel = pd.Series(myList,index=myLabels)
print(mySeriesWithLabel)
print(mySeriesWithLabel['b'])




# create Series from a dictionary
myDict = {'id':1,'first-name':'Sahar','last-name':'razavi'}
mySeriesFromDict = pd.Series(myDict)
print(mySeriesFromDict)





# create a DataFrame from two Series
productList=["White Paper", "Marker", "Envelope"]
priceList=[12.60,4.70,1.20]
productSeries=pd.Series(productList)
priceSeries=pd.Series(priceList)
productDataFrame=pd.DataFrame({
    "Product":productSeries,
    "Price":priceSeries,
})
print(productDataFrame)





# add a column (Series) to a DataFrame
dfProduct = pd.DataFrame({
  'product': ["White Paper", "Marker", "Envelope"],
  'price': [12.60,4.70,1.20]
})
cat = ["A","B","A"]
dfProduct['Category'] = pd.Series(cat)
print(dfProduct)
