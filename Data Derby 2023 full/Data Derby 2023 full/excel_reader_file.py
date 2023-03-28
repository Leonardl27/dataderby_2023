# import openpyxl
import openpyxl

# Load workbook, enter workbook name
workbook = openpyxl.load_workbook('Egges.xlsx')

# Select sheet by name, enter sheet name
sheet = workbook['BLS Data Series']

# Extract table, specify min_row, max_row, min_col, max_col
# These will be the table paramaters
table = []
for row in sheet.iter_rows(min_row=10, max_row=53, min_col=1, max_col=13):
    row_data = []
    for cell in row:
        row_data.append(cell.value)
    table.append(row_data)

# Print table
for row in table:
    print(row)
