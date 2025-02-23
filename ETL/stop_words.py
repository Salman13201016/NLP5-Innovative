#amar je sokol 
#word gulo rakhar dorkar nai segulok stop words bole

#it is a book
# [this,'is','a','book']

# stop_words = ['a','is','am']

# sample = ['this','is','a','book','hello']

# for i in sample:
#     if i not in stop_words:
#         print(i)

import pandas as pd 
from nltk.corpus import stopwords
import nltk 
nltk.download('stopwords')

stop_words_english = set(stopwords.words('english'))
print(stop_words_english)
print(len(stop_words_english))

data = {'text':['this is a NLP class!','we are at class #10']}

df = pd.DataFrame(data)

df['stop'] = df['text'].apply(lambda x: ' '.join(word for word in x.split() if word.lower() not in stop_words_english))

print(df['stop'])
