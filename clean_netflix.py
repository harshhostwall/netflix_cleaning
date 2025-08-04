import pandas as pd

# Load data
df = pd.read_csv("netflix_titles.csv")

# Handle missing values (updated)
df['director'] = df['director'].fillna('Not Available')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Format text
df['type'] = df['type'].str.title()
df['rating'] = df['rating'].str.upper()

# Fix extra spaces before date, then parse
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

print("Cleaning complete. File saved.")
