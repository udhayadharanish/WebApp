import folium
import pandas
v = pandas.read_csv("Volcanoes.txt")
lat = list(v["LAT"])
lon = list(v["LON"])
name = list(v["NAME"])
el = list(v["ELEV"])

def color(ele):
        if ele <1000:
            return 'green'
        elif 1000 <= ele < 2000:
            return 'orange'
        else:
            return 'red'

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,n,e in zip(lat,lon,name,el):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=n,fill_color=color(e),color="white",fill_opacity=1.0,radius=6))
fgp = folium.FeatureGroup(name="Outline")
fgp.add_child(folium.GeoJson(open("world.json",'r',encoding="utf-8-sig").read()))
fgpc = folium.FeatureGroup(name="Population")
fgpc.add_child(folium.GeoJson(open("world.json",'r',encoding="utf-8-sig").read(),style_function=lambda x : {"fillColor" : 'green' if x["properties"]["POP2005"] < 1000000
                                                                                                     else 'yellow' if 1000000 <= x["properties"]["POP2005"] < 2000000
                                                                                                     else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(fgpc)
map.add_child(folium.LayerControl())

map.save("map.html")