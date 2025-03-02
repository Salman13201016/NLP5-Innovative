import pandas as pd
import polars as pl
import requests
import sqlite3
from sqlalchemy import create_engine
from concurrent.futures import ThreadPoolExecutor

# 1. CSV ফাইল থেকে ডেটা লোড
def load_csv(file_path, use_polars=False):
    if use_polars:
        return pl.read_csv(file_path,encoding='ISO-8859-1')  # Polars দিয়ে লোড
    else:
        return pd.read_csv(file_path,encoding='ISO-8859-1')  # Pandas দিয়ে লোড

# 2. API থেকে ডেটা লোড
def load_api(api_url, use_polars=False):
    response = requests.get(api_url)  # API কল
    data = response.json()  # JSON ডেটা রিসিভ

    if use_polars:
        return pl.DataFrame(data)  # Polars দিয়ে লোড
    else:
        return pd.DataFrame(data)  # Pandas দিয়ে লোড

def load_multiple_sources(file_paths, api_url,use_polars=False):
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        # Load data from CSV files
        for file_path in file_paths:
            futures.append(executor.submit(load_csv, file_path, use_polars))
        
        # Load data from API
        futures.append(executor.submit(load_api, api_url, use_polars))
        results = [future.result() for future in futures]
    print(results)



# উদাহরণ ব্যবহার:
file_paths = ['sentiment140.csv', 'sentiment140_v2.csv']  # CSV ফাইল পাথ
api_url = 'https://jsonplaceholder.typicode.com/posts'  # API URL

results = load_multiple_sources(file_paths, api_url,use_polars=False)