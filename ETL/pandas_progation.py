# 1 ) Removing Rows/Columns - 50%=>
# 2) Imputation: Filling missing with something (Constant, mean, mode, median)
# 3) Propgation: Forward Propagation & Backward Propagation
# 4) Interpolation: Assignment - Linear/Polynomial

#assignment from Propagation: ffill with avg of recent 3 previous values. ffill with avg of all previous valus


import pandas as pd

data = {'id':[1,2,3,None,4], 'score':[10,20,30,23,None]
}

df = pd.DataFrame(data)
new_df = df.fillna(method='bfill')
df_copy = df.copy()

# for col in df_copy.columns:
#     if df_copy[col].isnull().any():
#         df_copy[col] = df_copy[col].fillna(df_copy[col]).median()

print(df)
print(new_df)
#remove the row or column if null value exists more than 49%