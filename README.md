Netflix Movies and TV Shows — Data Cleaning Summary:

-The file netflix_titles_cleaned.csv is the cleaned data
-The file clean_netflix.py is the python code I used to clean the data.
-Dropped rows missing critical data in date_added column.
-Filled missing values in director, cast, country, and rating columns with placeholders to maintain dataset integrity.
-Removed duplicate rows to avoid redundant entries.
-Standardized text fields by fixing capitalization in type and rating columns.
-Cleaned column headers: converted all to lowercase, replaced spaces with underscores for consistent naming.
-Trimmed whitespace from string fields to prevent formatting issues.
-Converted date_added to datetime format for easier time-based analysis.
-Ensured appropriate data types (e.g., integers for release year).

