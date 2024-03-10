import geopandas as gpd
import folium
from folium.plugins import MarkerCluster, HeatMap
from random import randrange

# Load shapefile
shapefile_path = "/Users/benjaminmichel/Desktop/Glasgow/shapefile/amenities/amenities.shp"
gdf = gpd.read_file(shapefile_path)

# Create a map centered on Glasgow
glasgow_map = folium.Map(location=[55.8642, -4.2518], zoom_start=12)

# Add the GeoDataFrame as a layer to the map with dynamically assigned colors
marker_cluster = MarkerCluster().add_to(glasgow_map)

# Generate random colors for each unique amenity type
unique_amenities = gdf['amenity'].unique()
colors = {amenity: "#{:06x}".format(randrange(0, 0xFFFFFF)) for amenity in unique_amenities}

for idx, row in gdf.iterrows():
    folium.Marker(
        location=[row['geometry'].y, row['geometry'].x],
        popup=row['amenity'],
        icon=folium.Icon(color=colors.get(row['amenity'], 'gray'))
    ).add_to(marker_cluster)

# Add legend based on dynamically detected amenity types
legend_html = """
<div style="position: fixed; top: 10px; right: 10px; z-index:1000; font-size:14px; background-color:white; border-radius:5px; padding: 10px; box-shadow: 2px 2px 2px #888888;">
<b>Legend</b><br>
"""

for amenity_type, color in colors.items():
    legend_html += f'<i style="background:{color}"></i> {amenity_type}<br>'

legend_html += "</div>"

glasgow_map.get_root().html.add_child(folium.Element(legend_html))

# Add LayerControl to the map
folium.LayerControl().add_to(glasgow_map)

# Create a density map analysis layer
heat_data = [[point.xy[1][0], point.xy[0][0]] for point in gdf.geometry]
HeatMap(heat_data, radius=15).add_to(glasgow_map)

# Save the map as an HTML file
glasgow_map.save("/Users/benjaminmichel/Desktop/Glasgow/glasgow_map.html")
