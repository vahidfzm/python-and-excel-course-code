###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook

from openpyxl.styles import Alignment



wb=load_workbook('lecture06-styles/list1.xlsx')
ws1=wb.active


alignment=Alignment(horizontal='center', vertical='center', text_rotation=30, wrap_text=False,shrink_to_fit=False,indent=0)



for row in ws1['A1:H1']:
    for c in row:
        c.alignment=alignment



wb.save(filename='lecture06-styles/list1Modified.xlsx')
