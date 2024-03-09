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
        popup=row['name'],  # Adjust 'HotelName' to the actual column name in your shapefile
    ).add_to(marker_cluster)

# Add legend using the file name
legend_html = """
<div style="position: fixed; bottom: 50px; right: 50px; z-index:1000; font-size:14px; background-color:white; border-radius:5px; padding: 10px; box-shadow: 2px 2px 2px #888888;">
<b>Legend</b><br>
File Name: hotel-point.shp
</div>
"""

glasgow_map.get_root().html.add_child(folium.Element(legend_html))

# Add LayerControl to the map
folium.map.LayerControl().add_to(glasgow_map)

# Save the map as an HTML file
glasgow_map.save("/Users/benjaminmichel/Desktop/Glasgow/glasgow_map.html")
