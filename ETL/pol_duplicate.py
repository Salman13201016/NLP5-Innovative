import polars as pl

data = {'id':[1,2,2,2,4,5,5,6],'score':[10,20,20,20,40,50,50,60]}

df = pl.DataFrame(data)

detect_dup = df.filter(pl.col('id').is_duplicated())

print(detect_dup)

rm_duplicate_keep_first = df.unique()
rm_duplicate_keep_last = df.unique(keep='last')

print(df)
print(rm_duplicate_keep_first)
print(rm_duplicate_keep_last)