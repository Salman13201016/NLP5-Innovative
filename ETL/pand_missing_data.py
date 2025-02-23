# 1 ) Removing Rows/Columns - 50%=>
# 2) Imputation: Filling missing with something (Constant, mean, mode, median)
# 3) Propgation: Forward Propagation & Backward Propagation
# 4) Interpolation: Assignment - Linear/Polynomial


import pandas as pd

data = {'id':[1,2,3,4], 'score':[10,20,30,None]
}

df = pd.DataFrame(data)

rm_row = df.dropna()

rm_col = df.dropna(axis=1)

print(df)
print(rm_row)
print(rm_col)

#remove the row or column if null value exists more than 49%