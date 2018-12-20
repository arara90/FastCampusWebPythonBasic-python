from openpyxl import load_workbook as load

dir = 'D:/FastCampus/FastCampusWebPythonBasic-python/code09_Excel/users.xlsx'
wb = load(dir)
ws = wb.create_sheet('구구단')

for i in range(2,9) :
    for j in range(1,9):
        res="{} x {} = {}"
        print(res.format(i,j,i*j))

for a in range( ord("a"),ord("h") ):
    print(a)