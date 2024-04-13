import pandas as pd
df1 = pd.read_excel("asm2.xlsx", sheet_name="oder")
df2 = pd.read_excel("asm2.xlsx", sheet_name="oderdetails")
# pd.set_option('display.max_rows', 120)
df=merged = pd.merge(df1, df2, on=['OrderID'])
print(df1, df2)