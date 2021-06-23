###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook

from openpyxl.styles import Protection

wb=load_workbook('lecture06-styles/list1.xlsx')
ws1=wb.active


protection=Protection(locked=False,hidden=False)

for row in ws1['D2:D20']:
    for c in row:
        c.protection=protection


ws1.protection.sheet=True
ws1.protection.password='12345'
ws1.protection.enable()
# ws1.protection.disable()


wb.save(filename='lecture06-styles/list1Modified.xlsx')
