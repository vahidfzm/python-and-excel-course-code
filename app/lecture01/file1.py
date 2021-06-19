###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import Workbook


# create a new workbook
wb=Workbook()


# set a name for the active sheet
ws1 = wb.active
ws1.title = "My Sheet"


# save the workbook
wb.save(filename='lecture01/file1.xlsx')
