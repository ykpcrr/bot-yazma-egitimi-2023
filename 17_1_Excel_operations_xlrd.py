import xlrd

# Open Excel File

work_book = xlrd.open_workbook("./datas/WorldCupPlayers.xls")

# Pick the first page
ws = work_book.sheet_by_name("WorldCupPlayers")

# Print value of first cell
print(ws.cell(0, 0).value)

# Print number of rows
print(ws.nrows)

# Print number of cols
print(ws.ncols)
events = []

for row in ws.get_rows():
    # players name RONALDO
    if row[6].value != "RONALDO":
        continue
    if row[8].value and (row[8].value.startswith("G") or row[8].value.startswith("P")):
        events.append(row[8].value)

print(len(events))
