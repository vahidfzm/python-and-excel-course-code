###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook



wb=load_workbook('lecture06-styles/list1.xlsx')
ws1=wb.active



for row in wb['Sheet2']['D2:D4']:
    for c in row:
        print(c.font)
        print(c.alignment)
        print(c.border)
        print('----------------------------------------')



wb.save(filename='lecture06-styles/list1Modified.xlsx')
