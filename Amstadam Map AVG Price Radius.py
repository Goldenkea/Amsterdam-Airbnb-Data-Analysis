import pandas as pd
import folium 

df = pd.read_csv(r'C:\Users\Nick\OneDrive\Desktop\Education\Other Education\Data Analytics\Amstadam Airbnb\filtered_listings.csv')

df_filtered = df[df['price'] < 100]

# City center coordinates
city_center = (52.374, 4.889)

# Initialize the map
m = folium.Map(location=city_center, zoom_start=12)

radius_ranges = [(5, 10),(2.5, 5),(0, 2.5)]  #(inner_radius, outer_radius)
colors = ['#025259', '#025259','#025259']  
info = ['Average Price for 5 - 10km: 219.51 Euro', 'Average Price for 2.5 - 5km: 247.80 Euro', 'Average Price for 0 - 2.5km: 328.44 Euro']

for (inner_radius, outer_radius), color, hover_info in zip(radius_ranges, colors, info):
    folium.Circle(
        location=city_center,
        radius=outer_radius * 1000,  # Convert km to meters
        color=color,
        fill=True,
        fill_opacity=0.1,
        opacity=0.5,
        tooltip=hover_info  # Tooltip for hover
    ).add_to(m)

for _, row in df_filtered.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=1,  # Adjust the size of the dot
        color='#D94F04',
        fill=True,
        fill_color='#D94F04',
        fill_opacity=0.1,
        popup=f"{row['name']}: €{row['price']}/night"
    ).add_to(m)
# Save the map to an HTML file``
m.save(r'C:\Users\Nick\OneDrive\Desktop\Education\Other Education\Data Analytics\Amstadam Airbnb\amsterdam_map.html')
