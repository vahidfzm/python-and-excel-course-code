###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook

from openpyxl.styles import Font


wb=load_workbook('lecture06-styles/list1.xlsx')
ws1=wb.active



font = Font(name='Tahoma',
                 size=22,
                 bold=True,
                 italic=False,
                 vertAlign=None,
                 underline='double',
                 strike=False,
                 color='00CCCCFF')


for row in ws1['A1:H1']:
    for c in row:
        c.font=font


wb.save(filename='lecture06-styles/list1Modified.xlsx')
