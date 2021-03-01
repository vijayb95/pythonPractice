import folium

# tiles = "Stamen Terrain"

map = folium.Map(location=[13.067439, 80], zoom_start=6, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name = 'my map')
fg.add_child(folium.Marker(location=[13.067439, 80], popup='This is a marker', icon=folium.Icon(color='darkgreen')))

map.add_child(fg)

map.save('Map1.html')