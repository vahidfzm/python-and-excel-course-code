###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook

from openpyxl.styles import  Border, Side



wb=load_workbook('lecture06-styles/list1.xlsx')
ws1=wb.active


side1=Side(border_style='thick',color='00FFFF00')
side2=Side(border_style='medium', color='0099CCFF')

border1=Border(left=side1,right=side1,top=side1,bottom=side1)
border2=Border(left=side2,right=side2,top=side2,bottom=side2)


for row in ws1['A3:H3']:
    for c in row:
        c.border=border1

for row in ws1['A6:H6']:
    for c in row:
        c.border=border2


wb.save(filename='lecture06-styles/list1Modified.xlsx')
