import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df['director'] = df['director'].fillna('Not Available')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

df = df.drop_duplicates()
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df['type'] = df['type'].str.title()
df['rating'] = df['rating'].str.upper()

df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

print("Cleaning complete. File saved.")
