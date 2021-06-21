###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook

wb=load_workbook('lecture04/list1.xlsx')

ws1=wb.active


# add a new column to the list1.xlsx file (Column I), 
# name it VAT and write a excel-formula to calculate it as 20% of Total price

ws1['I1']="VAT"


# option 1 which is not so nice!(manuall index)
# i=2
# for cell in ws1['I'][1:]:
#     cell.value="=H" + str(i) + " * 20%"
#     i=i+1


# option 2 which still is not the best
# for j in range(len(ws1['I'][1:])):
#     ws1['I' + str(j+2)]="=H" + str(j+2) + " * 20%"


# option 3, the best!
for j in range(len(ws1['I'][1:])):
    ws1['I{}'.format(j+2) ]="=H{} * 20%".format(j+2)


# more about text formatting in python
    

# set currency-format for the new added column 
for j in range(len(ws1['I'][1:])):
    ws1['I{}'.format(j+2)].number_format='"€"\ #,##0.00'




wb.save(filename='lecture04/list1Modified.xlsx')
