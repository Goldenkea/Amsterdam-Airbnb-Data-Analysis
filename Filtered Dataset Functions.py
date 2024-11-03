import pandas as pd

df = pd.read_csv(r'C:\Users\Nick\OneDrive\Desktop\Education\Other Education\Data Analytics\Amstadam Airbnb\listings.csv')

df = df[df['room_type'].isin(['Private room', 'Entire home/apt'])]

df = df[df['availability_365'] != 365]

df = df[df['license'].str.contains(r'^[A-Za-z0-9].*|^Exempt$', na=False)]

df = df[df['minimum_nights'] <= 3]



output_file_path = r'C:\Users\Nick\OneDrive\Desktop\Education\Other Education\Data Analytics\Amstadam Airbnb\filtered_listings.csv'
df.to_csv(output_file_path, index=False)