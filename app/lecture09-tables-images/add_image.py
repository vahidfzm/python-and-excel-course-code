###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import Workbook
from openpyxl.drawing.image import Image,PILImage

wb=Workbook()
ws1=wb.active

if PILImage:
    img=Image('/app/lecture09-tables-images/python-logo.png')
    img.width=200
    img.height=200
    ws1.add_image(img,'B5')


wb.save(filename='lecture09-tables-images/imageAdded.xlsx')


