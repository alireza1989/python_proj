import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

mapp = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el) + " m", radius=6, fill_color=color_producer(el), color='gray', fill_opacity=0.7))

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


mapp.add_child(fgv)
mapp.add_child(fgp)
mapp.add_child(folium.LayerControl())
mapp.save("map1.html")
