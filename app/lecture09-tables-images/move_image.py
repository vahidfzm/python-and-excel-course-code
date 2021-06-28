###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook
from openpyxl.drawing.image import Image,PILImage

wb=load_workbook('lecture09-tables-images/list1.xlsx')
ws2 = wb['Sheet2']

ws2._images[0].width=ws2._images[0].width*2
ws2._images[0].anchor='G12'


wb.save(filename='lecture09-tables-images/list1ImageMoved.xlsx')
