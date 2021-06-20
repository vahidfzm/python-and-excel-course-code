###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import Workbook


wb=Workbook()
ws1 = wb.active


# nothing to print in a blank sheet
for r in ws1.rows:
    print(r)

for c in ws1.columns:
    print(c)





# print rows and columns in the usedRange (A1:D15)
ws1['D6']="fardanesh.ir"    
for r in ws1.rows:
    print(r)

for c in ws1.columns:
    print(c)





# loop over a range
for r in ws1['A1:D4']:
    for cell in r:
        cell.value="Fardanesh.ir"




wb.save(filename='lecture03/file1.xlsx')
