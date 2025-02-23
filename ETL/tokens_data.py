#remvoing special characters
#remove Numbers
#remove url
#tokenization
#removing Stopwords
#case conversion - lowercase
#stemming/lemmatization


#remove_punctuations_numbers

#apply: column - ekta function k oi column er sokol valuete implement korte chan tokhn amra oi column er upor apply function use kori

import pandas as pd
data = {'text':['this is a NLP class!','we are at class #10']}

df = pd.DataFrame(data)

# print(df.columns)

df['tokens'] = df['text'].apply(lambda x: x.split()) 

print(df['tokens'])


# import polars as pl

# df_p = pl.DataFrame(data)
# print("polars before",df_p)

# df1 = df_p.with_columns(pl.col('text').str.replace(r'[^a-zA-Z\s]','',literal=False).alias('text'))

# print("polars after",df1)