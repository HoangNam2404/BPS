import pandas as pd
df = pd.read_excel("asm2.xlsx", sheet_name="customer")
pd.set_option('display.max_rows', 120)
# df = df.dropna()
duplicates = df.duplicated()
df= df.drop(df[duplicates].index)
print(df)


























