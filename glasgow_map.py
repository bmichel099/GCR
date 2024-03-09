# publish_map.py
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster

# Load shapefile
shapefile_path = "/Users/benjaminmichel/Desktop/Glasgow/hotel/hotel-point.shp"
gdf = gpd.read_file(shapefile_path)

# Create a map centered on Glasgow
glasgow_map = folium.Map(location=[55.8642, -4.2518], zoom_start=12)

# Add the GeoDataFrame as a layer to the map
marker_cluster = MarkerCluster().add_to(glasgow_map)
for idx, row in gdf.iterrows():
    folium.Marker(
        location=[row['geometry'].y, row['geometry'].x],
        popup=row['name']  # Adjust 'Name' to the actual column name in your shapefile
    ).add_to(marker_cluster)

# Save the map as an HTML file
glasgow_map.save("/Users/benjaminmichel/Desktop/Glasgow/glasgow_map.html")
