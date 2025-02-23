# 1 ) Removing Rows/Columns - 50%=>
# 2) Imputation: Filling missing with something (Constant, mean, mode, median)
# 3) Propgation: Forward Propagation & Backward Propagation
# 4) Interpolation: Assignment - Linear/Polynomial


import pandas as pd

data = {'id':[1,2,3,4], 'score':[10,20,30,None]
}

df = pd.DataFrame(data)
df_copy = df.copy()

for col in df_copy.columns:
    if df_copy[col].isnull().any():
        df_copy[col] = df_copy[col].fillna(df_copy[col]).median()

print(df)
print(df_copy)
#remove the row or column if null value exists more than 49%