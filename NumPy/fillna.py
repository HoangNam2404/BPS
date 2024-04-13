import pandas as pd
df = pd.read_excel("asm2.xlsx", sheet_name="oderdetails")
pd.set_option('display.max_rows', 120)
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0)
print(df)