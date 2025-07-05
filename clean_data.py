import pandas as pd
import numpy as np

df = pd.read_csv('/Users/titan/Desktop/Cinematch/imdb_top_1000.csv')
print(df.isna().sum())
import pandas as pd

# Load the dataset
df = pd.read_csv("imdb_top_1000.csv")

# Rename relevant columns
df.rename(columns={
    'Series_Title': 'Title',
    'Genre': 'Genres',
    'Overview': 'Plot',
    'IMDB_Rating': 'Rating'
}, inplace=True)

# Clean Genres - convert to list
df['Genres'] = df['Genres'].apply(lambda x: [genre.strip() for genre in x.split(',')])

# Clean runtime (optional, to keep just numbers)
df['Runtime'] = df['Runtime'].str.extract('(\d+)').astype(float)

# Convert Released Year and Rating to proper types
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Select only relevant columns
clean_df = df[['Title', 'Genres', 'Plot', 'Rating', 'Released_Year']]

# Save to new CSV
clean_df.to_csv("cleaned_movie_data.csv", index=False)

print("✅ Data cleaned and saved as 'cleaned_movie_data.csv'")

