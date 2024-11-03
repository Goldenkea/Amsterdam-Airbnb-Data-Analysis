import pandas as pd
from geopy.distance import great_circle

#Creating a Pandas dataframe with a CSV file:
df = pd.read_csv(r'__Retrieve_File_From_Path__')



#Average Price by distance from the City Center:
city_center = (52.374, 4.889)

def calculate_distance(row):
    return great_circle(city_center, (row['latitude'], row['longitude'])).kilometers
    #Haversine Formula

df['distance'] = df.apply(calculate_distance, axis=1)

avg_price_2_5km = df[df['distance'] <= 2.5]['price'].mean()
avg_price_2_5_5km = df[(df['distance'] >= 2.5) & (df['distance'] <= 5)]['price'].mean()
avg_price_5_10km = df[(df['distance'] > 5) & (df['distance'] <= 10)]['price'].mean()

print(f"Average Price for Private Rooms within 2.5 km: {avg_price_2_5km} Euro")
print(f"Average Price for Private Rooms within 2.5-5 km: {avg_price_2_5_5km} Euro")
print(f"Average Price for Private Rooms within 5-10 km: {avg_price_5_10km} Euro")




#Comparison of the number of apartments to private bedrooms when price is under 100 Euro
num_of_apartments = df[(df['room_type'] == 'Entire home/apt') & (df['price'] < 100)].shape[0]
num_of_private_rooms = df[(df['room_type'] == 'Private room') & (df['price'] < 100)].shape[0]

print(f"Number of listings for Entire home/apt under €100: {num_of_apartments}")
print(f"Number of listings for Private room under €100: {num_of_private_rooms}")



#Average number of reviews per month for apartments vs private rooms
avg_reviews_entire_home = df[df['room_type'] == 'Entire home/apt']['reviews_per_month'].mean()
avg_reviews_private_room = df[df['room_type'] == 'Private room']['reviews_per_month'].mean()

print(f"Average Number of Reviews per Month for Entire home/apt: {avg_reviews_entire_home:.2f}")
print(f"Average Number of Reviews per Month for Private room: {avg_reviews_private_room:.2f}")



#Three closest listings to the city center:
closest_listings = df.nsmallest(3, 'distance')
print(closest_listings[['id', 'name', 'room_type', 'price', 'distance']])
