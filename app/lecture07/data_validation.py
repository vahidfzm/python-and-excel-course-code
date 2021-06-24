###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation


wb = Workbook()
ws1 = wb.active



# list validation
dv1=DataValidation(type="list",formula1='"Asia,Africa,Europe,Australia,North America,South America,Antarctica"',allow_blank=True)
dv1.add('A1:A10')


# Whole numbers less than 20
dv2=DataValidation(type="whole",operator="greaterThan",formula1=20)
dv2.error="greater than 20 please!!!"
dv2.errorTitle="Stop"
dv2.add('B1:B10')



# decimal numbers between 0 and 1
dv3 = DataValidation(type="decimal",operator="between", formula1=0, formula2=1)
dv3.add('C1:C10')


# strings with maximum 8 characters
dv4 = DataValidation(type="textLength", operator="lessThanOrEqual", formula1=8)
dv4.add('D1:D10')


# custom validation: unique values in column E for the range E1:E10
dv5 = DataValidation(type="custom",formula1="=countif(E:E,$E1)<=1")
dv5.add('E1:E10')




ws1.add_data_validation(dv1)
ws1.add_data_validation(dv2)
ws1.add_data_validation(dv3)
ws1.add_data_validation(dv4)
ws1.add_data_validation(dv5)




wb.save(filename='lecture07/dataValidationOutput.xlsx')
