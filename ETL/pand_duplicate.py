import pandas as pd

data = {'id':[1,2,2,2,4,5,5,6],'score':[10,20,20,20,40,50,50,60]}

df = pd.DataFrame(data)

detect_dup = df[df.duplicated()]

rm_duplicate_keep_first = df.drop_duplicates()
rm_duplicate_keep_last = df.drop_duplicates(keep='last')

print(df)
print(rm_duplicate_keep_first)
print(rm_duplicate_keep_last)