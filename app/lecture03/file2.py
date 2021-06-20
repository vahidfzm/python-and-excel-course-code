###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook

wb=load_workbook('lecture03/list1.xlsx')

ws1=wb.active


# temp=[1,3,6,7,33,57,232,550]
# temp[1:3]
# temp[2:]
# temp[-1:]

# increase prices in the list1.xlsx (20%)
for r in ws1['G'][1:]:
    r.value=r.value*1.2


# append a group of values at the bottom of the active sheet
newRowData=('03.06.2020','West', 'Los Angeles', 'Cookies', 'Oatmeal Raisin', 288, 2.84)
ws1.append(newRowData)
ws1.append([4,6,7])


wb.save(filename='lecture03/list1Modified.xlsx')
