import pandas as pd
df = pd.read_excel("asm2.xlsx", sheet_name="customer")
pd.set_option('display.max_rows', 120)
# filtering_df = df[df["City"].isin(["New York City", "Redmond"])]
print(df)