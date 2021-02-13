import openpyxl
import xlrd
import pandas
df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0, engine='openpyxl')
print(df3)