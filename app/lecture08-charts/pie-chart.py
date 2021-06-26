###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook
from openpyxl.chart import PieChart, Reference, ProjectedPieChart

from copy import deepcopy



wb=load_workbook('lecture08-charts/data1.xlsx')
ws=wb['PieCharts']


pie=PieChart()
labels=Reference(ws,min_col=3,min_row=8,max_row=11)
data=Reference(ws,min_col=4,min_row=7,max_row=11)
pie.add_data(data,titles_from_data=True)
pie.set_categories(labels)
pie.title = "Pie Chart"

ws.add_chart(pie,"F7")






projected_pie = ProjectedPieChart()
projected_pie.type = "bar"

# split by position
projected_pie.splitType = "pos" 
projected_pie.splitPos = 3

labels = Reference(ws, min_col=3, min_row=17, max_row=23)
data = Reference(ws, min_col=4, min_row=17, max_row=23)
projected_pie.add_data(data, titles_from_data=True)
projected_pie.set_categories(labels)
projected_pie.title = "Pie of bar"
ws.add_chart(projected_pie, "F17")



projected_pie_copy=deepcopy(projected_pie)
projected_pie_copy.type="pie"
projected_pie_copy.title = "Pie of pie"
ws.add_chart(projected_pie_copy, "F27")





wb.save(filename='lecture08-charts/data1WithChart.xlsx')
