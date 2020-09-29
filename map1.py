import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, titles="MapBox")

fgv = folium.FeatureGroup(name="VolcanoesUS")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(
        location=[lt, ln], popup=folium.Popup(str(el)+" m", parse_html=True), icon=folium.Icon(color="green" if el > 2500 else "orange")))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {
              'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
