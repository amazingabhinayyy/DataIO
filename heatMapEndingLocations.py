import folium
from folium.plugins import HeatMap
import pandas as pd

months = ["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
startLat = []
startLng = []
markerlats = [ 41.880958, 41.894503, 41.95786652, 41.89225757, 41.9121263]
markerlngs = [ -87.616743, -87.617854, -87.64950514, -87.61203134, -87.63508213]
labels = ["DuSable Lake Shore Dr and Monroe Street","DuSable Lake Shore Dr and North Blvd", "Michigan Avenue and Oak Street", "Streeter Drive and Grand Avenue", "Wells Street and Concord Lane"]


for month in months:

        df = pd.read_csv(f'{month}.csv')

        startVals = df[['end_lat','end_lng']]

        for index,cell in startVals.iterrows():
             startLat.append(cell['end_lat'])
             startLng.append(cell['end_lng'])

   


# Example DataFrame (replace this with your actual data)
# Let's assume we have 3 points in Chicago for demonstration
data = {
    'lat': startLat,  # Example latitudes
    'lon': startLng  # Example longitudes
}
df = pd.DataFrame(data)
df = df.dropna(subset=['lat', 'lon'])
# Create a map centered at an average location in Chicago
chicago_map = folium.Map(location=[41.8781, -87.6298], zoom_start=25)

# Add the heatmap
heatmap = HeatMap(df[['lat', 'lon']], radius=10,  gradient={0.4: 'blue', 0.65: 'lime', 0.9: 'red'}) 
chicago_map.add_child(heatmap)
for lat, lng, label in zip(markerlats, markerlngs, labels):
    folium.Marker(
        [lat, lng],
        popup=label  # Adding a popup label for each marker
    ).add_to(chicago_map)

# Save to an HTML file
chicago_map.save('chicago_heatmap.html')
print("finished")

