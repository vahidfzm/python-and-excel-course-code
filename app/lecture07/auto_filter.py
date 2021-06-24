###############################################################
################# https://www.fardanesh.ir ####################
###############################################################


from openpyxl import load_workbook


wb=load_workbook('lecture07/list1.xlsx')
ws1=wb.active



ws1.auto_filter.ref="A1:H20"
ws1.auto_filter.add_filter_column(2, ["Boston", "Los Angeles"])



# sort ascending
ws1.auto_filter.add_sort_condition("G1:G20")
ws1.auto_filter.add_sort_condition("G1:G20",False)


# sort descending
ws1.auto_filter.add_sort_condition("G1:G20",True)



wb.save(filename='lecture07/list1Modified.xlsx')
